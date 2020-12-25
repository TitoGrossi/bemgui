from PyQt5.QtWidgets import QUndoCommand
from PyQt5.QtCore import Qt
import bemgui.model.geometry.dcel

class undoAddPoint(QUndoCommand):
    def __init__(self, scene, point):
        super(undoAddPoint, self).__init__()
        self.scene = scene
        self.point = point

    def undo(self):
        bemgui.model.geometry.dcel.Point.num_points_in_scene -= 1
        self.scene.removeItem(self.point)

    def redo(self):
        bemgui.model.geometry.dcel.Point.num_points_in_scene += 1
        self.point.idx = bemgui.model.geometry.dcel.Point.num_points_in_scene
        self.point.setZValue(bemgui.model.geometry.dcel.Point.base_z_value)
        self.scene.addItem(self.point)


class undoAddGeomElement(QUndoCommand):
    def __init__(self, scene, element, path):
        super(undoAddGeomElement, self).__init__()
        self.element = element
        self.scene = scene
        self.first_time = True
        self.element.setPath(path)

    def undo(self):
        self.element.update_neighbors_upon_delete()
        self.scene.removeItem(self.element)
        if self.element.half_edge.left is not None and self.element.half_edge.left.initialHalfEdge is not self.element.half_edge:
            self.element.half_edge.left.update()

    def redo(self):
        if self.first_time:
            self.first_time = False
        else:
            self.element.initialPoint.connectivity.add(self.element)
            self.element.finalPoint.connectivity.add(self.element)
            self.scene.addItem(self.element)
        self.element.setZValue(bemgui.model.geometry.dcel.Edge.base_z_value)
        self.element.finishPath(self.element.path())
        self.element.update_neighbors_upon_creation()
        if self.element.half_edge.previous.left:
            self.element.half_edge.previous.left.update()
        if self.element.half_edge.next.left:
            self.element.half_edge.next.left.update()


class undoBuildZone(QUndoCommand):
    def __init__(self, scene, zone, isClockwise):
        super(undoBuildZone, self).__init__()
        self.scene = scene
        self.zone = zone
        self.isClockwise = isClockwise

    def undo(self):
        bemgui.model.geometry.dcel.Zone.num_zones_in_scene -= 1
        self.scene.removeItem(self.zone)
        for half_edge in self.zone.traverse_outer():
            half_edge.left = None
        if self.zone.isMaster and not self.zone.is_clockwise():
            self.scene.setBackgroundBrush(Qt.white)
        if not self.zone.isMaster:
            self.zone.scene().master_zone.inner_components.remove(self.zone)

    def redo(self):
        bemgui.model.geometry.dcel.Zone.num_zones_in_scene += 1
        if self.isClockwise:
            self.zone.create()
        else:
            self.zone.create('ccw')
        self.zone.setZValue(bemgui.model.geometry.dcel.Zone.base_z_value + bemgui.model.geometry.dcel.Zone.num_zones_in_scene)
        self.scene.addItem(self.zone)
        if self.zone.isMaster and not self.zone.is_clockwise():
            self.zone.setBrush(Qt.white)
            self.zone.scene().setBackgroundBrush(Qt.gray)
        if not self.zone.isMaster:
            self.zone.scene().master_zone.inner_components.add(self.zone)


class undoUpdateZone(QUndoCommand):
    def __init__(self, zone, new_youngModule, new_poissonCoeficient, new_isCw, new_type):
        super(undoUpdateZone, self).__init__()
        self.zone = zone
        self.old_initialHalfEdge = zone.initialHalfEdge
        self.old_youngModule = zone.youngModule
        self.old_poissonCoeficient = zone.poissonCoeficient
        self.old_direction = self.zone.is_clockwise()
        self.old_type = self.zone.isHole

        self.new_youngModule = new_youngModule
        self.new_poissonCoeficient = new_poissonCoeficient
        self.new_isCw = new_isCw
        self.new_type = new_type
        if self.new_isCw != self.old_direction:
            self.new_initialHalfEdge = self.old_initialHalfEdge.twin
        else:
            self.new_initialHalfEdge = None

    def undo(self):
        self.zone.updateConstants(self.old_youngModule, self.old_poissonCoeficient)
        self.zone.updateBrush(self.old_type, self.old_direction)
        self.zone.updatePath(self.old_initialHalfEdge)


    def redo(self):
        self.zone.updateConstants(self.new_youngModule, self.new_poissonCoeficient)
        if self.new_initialHalfEdge:
            self.zone.updateBrush(self.new_type, self.new_isCw)
            self.zone.updatePath(self.new_initialHalfEdge)



class undoGenerateMesh(QUndoCommand):
    def __init__(self, scene):
        super(undoGenerateMesh, self).__init__()
        self.scene = scene

    def undo(self):
        pass

    def redo(self):
        pass


class undoAddDisplacementCondition(QUndoCommand):
    def __init__(self, scene):
        pass

    def undo(self):
        pass

    def redo(self):
        pass
