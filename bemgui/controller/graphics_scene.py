'''
Module that contains the scene class, which the applies the logic (control) of
the actions taken by the user in the scene of the application, as well as dealing
with the actual items that are added to the scene
'''

from PyQt5.QtWidgets import QGraphicsScene
from PyQt5 import QtGui, QtCore
from bemgui.model.geometry import dcel
from bemgui.model.geometry import edges
from bemgui.controller import undo_actions
# import bemgui.controller.undo_actions

class Scene(QGraphicsScene):
    def __init__(self, mainwindow):
        #Setting basics of QGraphicsScene (initalizing and setting rect
        QGraphicsScene.__init__(self, parent=None)
        self.setSceneRect(-100, -100, 100, 100)
        self.setParent(mainwindow)

        #Creating lists that will be used to write file
        self.currentItem = None

        #State of scene (what it is drawing)
        self.actions = {
            'addingPoint': {'press': self.addPoint,
                            'move': set()},
            'drawingLine': {'press': self.drawPath,
                            'move': {self.updatePath}},
            'drawingArc': {'press': self.drawPath,
                            'move': {self.updatePath}},
            'drawingQuadratic': {'press': self.drawPath,
                                 'move': {self.updatePath}},
            'drawingCubic': {'press': self.drawPath,
                             'move': {self.updatePath}},
            'definingZone': {'press': self.updateZone,
                            'move': set()}
        }
        self.currentAction = None
        self.clicked = False

        self.master_zone = None

    def addPoint(self, eventPos):
        '''
        Adds point to the scene
        '''
        point = dcel.Point(eventPos)
        point.setZValue(2)
        cmd = undo_actions.undoAddPoint(self, point)
        self.parent().undoStack.push(cmd)

    def cancel_drawing(self, message=None):
        '''
        Cancel drawing upon user action or error (drawn a prohibited edge)
        '''
        self.removeItem(self.currentItem)
        self.currentItem = None
        self.clicked = False
        if message:
            self.parent().status_bar.show_message(message)

    def has_master_zone(self):
        '''
        Function to tell if the scene has already a master zone drawin in it
        '''
        if dcel.Zone.num_zones_in_scene == 0:
            return False
        return True

    def create_new_zone(self, cmd_add_path):
        '''
        Function that creates a new zone upon detection (in the finishPath function)
        and generates a macro for the undoStack of mainwindow, which adds the newly
        added edge (from the cmd_add_path parameter, created in the finishPath function),
        as well as the zone itself
        '''
        self.parent().undoStack.beginMacro('Creating zone')
        self.parent().undoStack.push(cmd_add_path)
        zone_type, young, poisson, orientation = self.parent().showZoneWindow(not self.has_master_zone())
        zone = dcel.Zone(zone_type==1, self.currentItem.half_edge, zone_type==2, young, poisson)
        if not self.has_master_zone():
            self.master_zone = zone
        cmd_build_zone = undo_actions.undoBuildZone(self, zone, orientation)
        self.parent().undoStack.push(cmd_build_zone)
        self.parent().undoStack.endMacro()

    def drawPath(self, eventPos):
        if not self.clicked:
            self.initiatePath(eventPos)
        elif self.clicked + 1 == type(self.currentItem).num_points_to_complete:
            self.finishPath(eventPos)
        else:
            point = self.itemAt(eventPos, QtGui.QTransform())
            if type(point) is not dcel.Point:
                point = None
            self.updatePath(eventPos, point)

    def initiatePath(self, eventPos):
        point = self.itemAt(eventPos, QtGui.QTransform())
        if point and type(point) is dcel.Point:
            if self.currentAction == 'drawingLine':
                graphicalPath = edges.straightEdge(initialPoint=point)
            elif self.currentAction == 'drawingArc':
                graphicalPath = edges.arcEdge(initialPoint=point)
            elif self.currentAction == 'drawingQuadratic':
                graphicalPath = edges.quadraticEdge(initialPoint=point)
            elif self.currentAction == 'drawingCubic':
                graphicalPath = edges.cubicEdge(initialPoint=point)
            self.addItem(graphicalPath)
            self.currentItem = graphicalPath
            self.currentItem.setZValue(1)
            self.clicked = True

    def updatePath(self, eventPos, point=None):
        '''
        Passes the responsibility of updating path to the actual currentItem attribute
        '''
        if type(self.currentItem) is edges.straightEdge:
            self.currentItem.update(eventPos, point)
        else:
            self.currentItem.update(eventPos, self.clicked, point)
            if point:
                self.clicked += 1

    def is_ok_finishing_path(self, is_cyclic_init, is_cyclic_final):
        '''
        Function that checks border sharing and intersections upon finishing edge
        drawings
        '''
        if self.currentItem.intesects_with_any():
            self.cancel_drawing('This line collides with at least one other line')
            return False
        if type(self.currentItem) is edges.cubicEdge and self.currentItem.self_intersects():
            self.cancel_drawing('This edge self intersects')
            return False
        # Checking for cycles to see if the graphical element can be drawn based on cyclit points (DFS)
        if is_cyclic_init and is_cyclic_final:
            # self.cancel_drawing('You can\'t create another zone that has a border with the alreay created zone')
            self.cancel_drawing('You can\'t divide the zone into two')
            return False
        return True

    def finishPath(self, eventPos):
        '''
        Actions that are needed to be taken when user finishes drawing an edge
        '''
        point = self.itemAt(eventPos, QtGui.QTransform())
        if point and type(point) is dcel.Point:
            self.updatePath(point.position, point)
            is_cyclic_init = self.currentItem.initialPoint.isCyclic(set(), None)
            is_cyclic_final = self.currentItem.finalPoint.isCyclic(set(), None)
            if not self.is_ok_finishing_path(is_cyclic_init, is_cyclic_final):
                return
            self.currentItem.initialPoint.add_connection(self.currentItem)
            self.currentItem.finalPoint.add_connection(self.currentItem)
            cmd_add_path = undo_actions.undoAddGeomElement(self, self.currentItem, self.currentItem.path())
            just_formed_new_zone = self.currentItem.initialPoint.isCyclic(set(), None) and not is_cyclic_init
            # If we just formed a new zone, call create_new_zone function
            if just_formed_new_zone:
                self.create_new_zone(cmd_add_path)
            # Otherwise, just add new element to scene. If this addition updates
            # a zone, we deal with that on undo/redo classes
            else:
                self.parent().undoStack.push(cmd_add_path)
            self.currentItem = None
            self.clicked = False

    def updateZone(self, eventPos):
        zone = self.itemAt(eventPos, QtGui.QTransform())
        if zone and type(zone) is dcel.Zone:
            zone_type, young, poisson, isCw = self.parent().showZoneWindow(zone.isMaster)
            update_zone_action = undo_actions.undoUpdateZone(zone, young, poisson, isCw, zone_type)
            self.parent().undoStack.push(update_zone_action)

    def mousePressEvent(self, event):
        if not self.currentAction and event.modifiers() != QtCore.Qt.ControlModifier:
            for item in self.selectedItems():
                item.setPen(QtCore.Qt.black)
        if event.buttons() == QtCore.Qt.LeftButton and self.currentAction:
            self.actions[self.currentAction]['press'](event.scenePos())
        super(Scene, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.currentAction:
            if self.clicked:
                for side_command in self.actions[self.currentAction]['move']:
                    side_command(event.scenePos())
        self.parent().xPos.setText(str(round(event.scenePos().x()/1000, 3)))
        self.parent().yPos.setText(str(round(-event.scenePos().y()/1000, 3)))
        super(Scene, self).mouseMoveEvent(event)

    def get_zones(self):
        zones = {item for item in self.items() if item.zValue() < 0}
        return zones
