'''
Module to represent the basic graphical elements of the geometric package (point,
edge and zone) and all the logic related to them (both on a view and a model
perpective)
'''

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPointF, QRectF, pyqtSignal, QLineF


class point(QtWidgets.QGraphicsEllipseItem):
    '''
    Class to represent the points (nodes) which will be part of the plane graph
    and will have visual representation in the graphicsView (client area)
    '''
    base_z_value = 2
    num_points_in_scene = 0
    def __init__(self, pos):
        QtWidgets.QGraphicsEllipseItem.__init__(self, pos.x() - 4, pos.y() - 4, 8, 8)
        self.position = QPointF(pos.x(), pos.y())
        self.connectivity = set()

        self.setAcceptHoverEvents(True)
        self.setBrush(Qt.black)

    def __repr__(self):
        '''
        Debbuging and visualization purposes
        '''
        return f'class point idx <{self.idx}>'

    def isCyclic(self, visited, parent):
        '''
        Function to know if the instance of this class has a cycle connected to
        it
        '''
        # Append self to the list of visited nodes
        visited.add(self)
        # For each vertex connected to self
        for conn in self.connectivity:
            # Because lines in graphicsScene have directions, but we are treating
            # them as part of an undirected graph, we have to check which of the
            # vertex edges is self
            if self is conn.initialPoint:
                next_point = conn.finalPoint
            else:
                next_point = conn.initialPoint
            if next_point not in visited:
                # If the other node of the edge is not visited, call recursion
                # on that node with parent as self
                if next_point.isCyclic(visited, self):
                    return True
            elif parent is not next_point:
                # If next point is already visited but is not self's parent, return True
                return True
        return False

    def add_connection(self, element):
        self.connectivity.add(element)

    def searchEdgeNext(self, half_edge, edge):
        if len(self.connectivity) == 1:
            return half_edge.twin
        ordered_adjacency = self.orderByEdge(edge)
        if ordered_adjacency[0].half_edge.init_point is half_edge.twin.init_point:
            return ordered_adjacency[0].half_edge
        return ordered_adjacency[0].half_edge.twin

    def searchEdgePrevious(self, half_edge, edge):
        if len(self.connectivity) == 1:
            return half_edge.twin
        ordered_adjacency = self.orderByEdge(edge)
        if ordered_adjacency[-1].half_edge.twin.init_point is half_edge.init_point:
            return ordered_adjacency[-1].half_edge
        return ordered_adjacency[-1].half_edge.twin

    def orderByEdge(self, edge, direction='cw'):
        '''
        order the edges in relation to 'edge', in the specified direction.
        Especially, the next element is at result[0] and the previous at result[-1]
        '''
        list_connectivity = list(self.connectivity)
        angles = []
        for adjacency in list_connectivity:
            if adjacency.initialPoint is self:
                angles.append(adjacency.half_edge.angleAtPercent(0))
            else:
                angles.append(adjacency.half_edge.twin.angleAtPercent(0))
        if direction == 'cw':
            l = sorted(zip(list_connectivity, angles), key=lambda e: e[1])
        elif direction == 'ccw':
            l = sorted(zip(list_connectivity, angles), key=lambda e: e[1], reverse=True)
        l = [i[0] for i in l]
        ind = l.index(edge)
        result = []
        for i in range(ind+1, len(l)):
            result.append(l[i])
        for i in range(ind):
            result.append(l[i])
        return result

    def hoverEnterEvent(self, event):
        self.setPen(Qt.red)
        self.setBrush(Qt.red)

    def hoverLeaveEvent(self, event):
        self.setPen(Qt.black)
        self.setBrush(Qt.black)


class edge(QtWidgets.QGraphicsPathItem):
    '''
    Base of graphical elements, all elements applied to visualization inherits
    from this class
    '''
    # static member of class for z value placement
    base_z_value = 0
    def __init__(self, initialPoint=None, finalPoint=None):
        QtWidgets.QGraphicsPathItem.__init__(self)
        self.initialPoint = initialPoint
        self.finalPoint = finalPoint
        pen = QtGui.QPen(Qt.blue, 2)
        self.setPen(pen)

    def __repr__(self):
        '''Debbuging purposes'''
        if self.path().elementAt(1).type == 1:
            pathType = 'Line'
        else:
            pathType = 'Curve'
        return f'Path({pathType}, {self.initialPoint}, {self.finalPoint})'

    def finishPath(self, path):
        '''
        Deals with half_edge logic before setting the path to path
        '''
        if not hasattr(self, 'half_edge'):
            self.half_edge = path
            self.half_edge_reversed = path.toReversed()
        setattr(self.half_edge, 'twin', self.half_edge_reversed)
        setattr(self.half_edge, 'init_point', self.initialPoint)
        setattr(self.half_edge, 'left', None)
        setattr(self.half_edge_reversed, 'twin', self.half_edge)
        setattr(self.half_edge_reversed, 'init_point', self.finalPoint)
        setattr(self.half_edge_reversed, 'left', None)

        setattr(self.half_edge, 'next', self.finalPoint.searchEdgeNext(self.half_edge, self))
        setattr(self.half_edge, 'previous', self.initialPoint.searchEdgePrevious(self.half_edge, self))

        setattr(self.half_edge_reversed, 'next', self.initialPoint.searchEdgeNext(self.half_edge_reversed, self))
        setattr(self.half_edge_reversed, 'previous', self.finalPoint.searchEdgePrevious(self.half_edge_reversed, self))

        if self.half_edge.previous.left:
            self.half_edge.left = self.half_edge.previous.left
        if self.half_edge_reversed.previous.left:
            self.half_edge_reversed.left = self.half_edge_reversed.previous.left

        if len(self.initialPoint.connectivity) > 1:
            self.half_edge.previous.next = self.half_edge
            self.half_edge_reversed.next.previous = self.half_edge_reversed
        if len(self.finalPoint.connectivity) > 1:
            self.half_edge.next.previous = self.half_edge
            self.half_edge_reversed.previous.next = self.half_edge_reversed
        super(edge, self).setPath(path)

    def update_neighbors_upon_creation(self):
        '''
        Method used when the path of the edge is finished (first drawn or
        redo action)
        '''
        self.half_edge.previous.next = self.half_edge
        self.half_edge_reversed.next.previous = self.half_edge_reversed
        self.half_edge.next.previous = self.half_edge
        self.half_edge_reversed.previous.next = self.half_edge_reversed

    def update_neighbors_upon_delete(self):
        '''
        Method used when the edge is removed from the scene (undo action)
        '''
        self.initialPoint.connectivity.remove(self)
        self.finalPoint.connectivity.remove(self)
        self.half_edge.previous.next = self.half_edge.next
        self.half_edge.next.previous = self.half_edge.previous
        self.half_edge_reversed.previous.next = self.half_edge_reversed.next
        self.half_edge_reversed.next.previous = self.half_edge_reversed.next


class zone(QtWidgets.QGraphicsPathItem):
    '''
    Class that represents a region in a doubly-connected edge list, pointing to
    the initial half_edge, but also containing graphical properties and methods
    to change path or orientation
    '''
    base_z_value = -1000
    num_zones_in_scene = 0
    def __init__(self, isMaster, initialHalfEdge, isHole, youngModule=0, poissonCoeficient=0):
        QtWidgets.QGraphicsPathItem.__init__(self)
        self.initialHalfEdge = initialHalfEdge
        self.isMaster = isMaster
        self.isHole = isHole
        if self.isMaster:
            self.setBrush(QtGui.QBrush(Qt.gray, Qt.SolidPattern))
        elif self.isHole:
            self.setBrush(QtGui.QBrush(Qt.white, Qt.SolidPattern))
        else:
            self.setBrush(QtGui.QBrush(Qt.yellow, Qt.Dense5Pattern))
        self.youngModule = youngModule
        self.poissonCoeficient = poissonCoeficient

    def updateConstants(self, new_youngModule, new_poissonCoeficient):
        self.youngModule = new_youngModule
        self.poissonCoeficient = new_youngModule

    def updateBrush(self, isHole, direction):
        if self.isMaster:
            if self.isClockwise() and not direction:
                self.updatePath(new_initial_half_edge=self.initialHalfEdge.twin)
                self.setBrush(QtGui.QBrush(Qt.white, Qt.SolidPattern))
                self.scene().setBackgroundBrush(Qt.gray)
            elif not self.isClockwise() and direction:
                self.updatePath(new_initial_half_edge=self.initialHalfEdge.twin)
                self.setBrush(QtGui.QBrush(Qt.gray, Qt.SolidPattern))
                self.scene().setBackgroundBrush(Qt.white)
        else:
            self.isHole = isHole == 2
            if self.isHole:
                self.setBrush(QtGui.QBrush(Qt.white, Qt.SolidPattern))
            else:
                self.setBrush(QtGui.QBrush(Qt.yellow, Qt.Dense5Pattern))

    def updatePath(self, new_initial_half_edge=None):
        '''
        Update path based on new lines beeing added to it (maybe with a new
        initial half edge, if the idea is to change the orientation of the zone)
        '''
        if new_initial_half_edge:
            self.initialHalfEdge = new_initial_half_edge
        path = QtGui.QPainterPath()
        half_edges = self.traverse()
        for he in half_edges:
            he.left = self
            path.connectPath(he)
        self.setPath(path)

    def create(self, direction='cw'):
        '''
        Sets path upon creation based on the direction that needs to be traversed
        '''
        isCw = self.isClockwise()
        if (direction == 'ccw' and isCw) or (direction == 'cw' and not isCw):
            self.updatePath(self.initialHalfEdge.twin)
        else:
            self.updatePath()

    def traverse(self):
        '''
        Traverse the zone from the edge it points to, stored in
        self.initialHalfEdge
        '''
        originPoint = self.initialHalfEdge.init_point
        curr_edge = self.initialHalfEdge
        while True:
            nextPoint = curr_edge.twin.init_point
            yield curr_edge
            if nextPoint is originPoint:
                break
            curr_edge = curr_edge.next

        # If there is a crack on the origin point, add to path (degenerate case)
        if curr_edge.next is not self.initialHalfEdge:
            curr_edge = curr_edge.next
            nextPoint = curr_edge.twin.init_point
            while True:
                yield curr_edge.next
                curr_edge = curr_edge.next
                if nextPoint is originPoint:
                    break
                nextPoint = curr_edge.twin.init_point

    def isClockwise(self):
        '''
        Function to check in what direction we are traversing the zone.
        Returns True if traversing clockwise and False if counterclockwise
        '''
        line1 = QLineF(self.initialHalfEdge.pointAtPercent(0.5), QPointF(10000, 10000))
        line1.setAngle(self.initialHalfEdge.angleAtPercent(0.5))
        line2 = QLineF(self.initialHalfEdge.next.pointAtPercent(0.5), QPointF(10000, 10000))
        line2.setAngle(self.initialHalfEdge.next.angleAtPercent(0.5))
        intersection_type = line1.normalVector().intersect(line2.normalVector(), QPointF())
        if intersection_type == 2:
            return True
        elif intersection_type == 1:
            return False
