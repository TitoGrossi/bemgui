class displacementConstrain(QtWidgets.QGraphicsItemGroup):
    def __init__(self, direction, point):
        QtWidgets.QGraphicsItemGroup.__init__(self)
        self.direction = direction
        self.point = point
        self.pen = QtGui.QPen(Qt.green, 2)
        if 1 in self.direction:
            line1 = QtWidgets.QGraphicsLineItem()
            line1.setLine(self.point.position.x(), self.point.position.y(), self.point.position.x() - 20,
                          self.point.position.y() + 10)
            line1.setPen(self.pen)
            line2 = QtWidgets.QGraphicsLineItem()
            line2.setLine(self.point.position.x(), self.point.position.y(), self.point.position.x() - 20,
                          self.point.position.y() - 10)
            line2.setPen(self.pen)
            line3 = QtWidgets.QGraphicsLineItem()
            line3.setLine(line2.line().p2().x(), line2.line().p2().y(), line1.line().p2().x(), line1.line().p2().y())
            line3.setPen(self.pen)
            self.addToGroup(line1)
            self.addToGroup(line2)
            self.addToGroup(line3)
        if 2 in direction:
            line1 = QtWidgets.QGraphicsLineItem()
            line1.setLine(self.point.position.x(), self.point.position.y(), self.point.position.x() - 10,
                          self.point.position.y() + 20)
            line1.setPen(self.pen)
            line2 = QtWidgets.QGraphicsLineItem()
            line2.setLine(self.point.position.x(), self.point.position.y(), self.point.position.x() + 10,
                          self.point.position.y() + 20)
            line2.setPen(self.pen)
            self.addToGroup(line1)
            self.addToGroup(line2)
            line3 = QtWidgets.QGraphicsLineItem()
            line3.setLine(line2.line().p2().x(), line2.line().p2().y(), line1.line().p2().x(), line1.line().p2().y())
            line3.setPen(self.pen)
            self.addToGroup(line3)

    def updateConstrain(self, direction):
        pass


class traction(QtWidgets.QGraphicsItemGroup):
    def __init__(self, element, value):
        QtWidgets.QGraphicsItemGroup.__init__(self)
        self.element = element
        self.value = value
        self.pen = QtGui.QPen(Qt.cyan, 1)
        if type(element) == meshElement:
            path = element.path()
            for i in np.linspace(0, 1, endpoint=True, num=7):
                lineGeometry = QLineF()
                lineGeometry.setP1(path.pointAtPercent(i))
                lineGeometry.setLength(10)
                if self.value > 0:
                    lineGeometry.setAngle(path.angleAtPercent(i) - 90)
                else:
                    lineGeometry.setAngle(path.angleAtPercent(i) + 90)
                line = QtWidgets.QGraphicsLineItem()
                line.setLine(lineGeometry)
                arrow1Line = QLineF()
                arrow1Line.setP1(line.line().p2())
                arrow1Line.setLength(4)
                arrow1Line.setAngle(line.line().angle() - 225)
                arrow1 = QtWidgets.QGraphicsLineItem()
                arrow1.setLine(arrow1Line)
                arrow1.setPen(self.pen)
                self.addToGroup(arrow1)
                arrow2Line = QLineF()
                arrow2Line.setP1(QPointF(line.line().p2()))
                arrow2Line.setLength(4)
                arrow2Line.setAngle(line.line().angle() + 225)
                arrow2 = QtWidgets.QGraphicsLineItem()
                arrow2.setLine(arrow2Line)
                arrow2.setPen(self.pen)
                self.addToGroup(arrow2)
                line.setPen(self.pen)
                self.addToGroup(line)
            text = QtWidgets.QGraphicsSimpleTextItem()
            text.setText('{} {}'.format(str(self.value), 'MPa'))
            text.setPos(path.pointAtPercent(0.5))
            self.addToGroup(text)
        elif type(element) == meshExtremityPoint or type(element) == meshMiddlePoint:
            pass

        self.element.scene().addItem(self)

    def updateTraction(self, value):
        pass
