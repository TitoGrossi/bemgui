from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class meshElement(QtWidgets.QGraphicsItemGroup):
    num_elem = 0
    def __init__(self, initialPoint, middlePoint, finalPoint):
        super(meshElement, self).__init__()
        self.initialPoint = initialPoint
        self.middlePoint = middlePoint
        self.finalPoint = finalPoint
        self.st_line = QtWidgets.QGraphicsLineItem(initialPoint.pos().x(), initialPoint.pos().y(), middlePoint.pos().x(), middlePoint.pos().y())
        self.nd_line = QtWidgets.QGraphicsLineItem(middlePoint.pos().x(), middlePoint.pos().y(), finalPoint.pos().x(), finalPoint.pos().y())
        self.addToGroup(self.st_line)
        self.addToGroup(self.nd_line)

        meshElement.num_elem += 1
        self.idx = meshElement.num_elem

        self.force = None

        self.setAcceptHoverEvents(True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)

    def hoverEnterEvent(self, event):
        '''
        highlights element, if it is not already selected
        '''
        if not self.isSelected():
            self.setPen(Qt.red)

    def hoverLeaveEvent(self, event):
        '''
        unhighlights element, if it is not already selected
        '''
        if not self.isSelected():
            self.setPen(Qt.black)

    def setPen(self, pen):
        '''
        sets 'pen' to all its children
        '''
        for item in self.childItems():
            item.setPen(pen)

    def mousePressEvent(self, event):
        '''
        Deals with scene's item selection logic, giving it a green color if it
        is selected and removing the same color from all other selected items if
        ctrl (or cmd) is not pressed
        '''
        if event.modifiers() != Qt.ControlModifier:
            for item in self.scene().selectedItems():
                item.setPen(Qt.black)
        super(meshElement, self).mousePressEvent(event)
        for item in self.childItems():
            item.setPen(Qt.green)

    def shape(self):
        '''
        Together with boundingRect(), this function is implemented for more
        fine grained mouse hit detection for user selection
        '''
        return self.st_line.shape().united(self.nd_line.shape())

    def boundingRect(self):
        '''
        Together with shape(), this function is implemented for more fine
        grained mouse hit detection for user selection. In fact, it only returns
        the bounding the rection of the path calculated in shape
        '''
        return self.shape().boundingRect()


class meshPoint():
    '''
    Virtual class responsible for having a common namespace between the two types
    of mesh points (meshExtremityPoint and meshMiddlePoint) and keeping an index
    of those for easy file generation
    '''
    num_points = 0
    def __init__(self):
        meshPoint.num_points += 1
        self.idx = meshPoint.num_points
        self.force = None

    def __del__(self):
        meshPoint.num_points -= 1


class meshExtremityPoint(QtWidgets.QGraphicsItemGroup, meshPoint):
    def __init__(self, position, rotation):
        super(meshPoint, self).__init__()
        QtWidgets.QGraphicsEllipseItem.__init__(self)
        self.position = position
        self.rotation = rotation
        line1 = QtWidgets.QGraphicsLineItem()
        line1.setLine(self.position.x() - 2.5, self.position.y() + 2.5,
                      self.position.x() + 2.5, self.position.y() - 2.5)
        line1.setTransformOriginPoint(self.position.x(), self.position.y())
        line1.setRotation(self.rotation + 90)
        self.addToGroup(line1)
        line2 = QtWidgets.QGraphicsLineItem()
        line2.setLine(self.position.x() - 2.5, self.position.y() - 2.5,
                      self.position.x() + 2.5, self.position.y() + 2.5)
        line2.setTransformOriginPoint(self.position.x(), self.position.y())
        line2.setRotation(self.rotation + 90)
        self.addToGroup(line2)

        self._displacement = None
        self._forces = None

    def setPen(self, pen):
        for line in self.childItems():
            line.setPen(pen)

    def pos(self):
        return self.position

    def updateDisplacement(self, displacement):
        self._displacement = displacement

    def getDisplacement(self):
        return {1, 2, 3}

    def updateForces(self, force):
        self._forces = force


class meshMiddlePoint(QtWidgets.QGraphicsEllipseItem, meshPoint):
    def __init__(self, position):
        super(meshPoint, self).__init__()
        QtWidgets.QGraphicsEllipseItem.__init__(self, position.x() - 2, position.y() - 2, 4, 4)
        self.position = position

    def pos(self):
        return self.position
