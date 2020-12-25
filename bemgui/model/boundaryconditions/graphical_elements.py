from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QGraphicsLineItem, QGraphicsTextItem, QGraphicsItemGroup
from PyQt5.QtCore import Qt, QLineF

class displacementConstrain(QGraphicsItemGroup):
    pen = QPen(Qt.green, 2)
    def __init__(self, direction, point):
        super(displacementConstrain, self).__init__()
        self.direction = direction
        self.point = point
        if 1 in self.direction:
            line1 = QGraphicsLineItem()
            line1.setLine(self.point.position.x(), self.point.position.y(), self.point.position.x() - 20,
                          self.point.position.y() + 10)
            line1.setPen(displacementConstrain.pen)
            line2 = QGraphicsLineItem()
            line2.setLine(self.point.position.x(), self.point.position.y(), self.point.position.x() - 20,
                          self.point.position.y() - 10)
            line2.setPen(displacementConstrain.pen)
            line3 = QGraphicsLineItem()
            line3.setLine(line2.line().p2().x(), line2.line().p2().y(), line1.line().p2().x(), line1.line().p2().y())
            line3.setPen(self.pen)
            self.addToGroup(line1)
            self.addToGroup(line2)
            self.addToGroup(line3)
        if 2 in direction:
            line1 = QGraphicsLineItem()
            line1.setLine(self.point.position.x(), self.point.position.y(), self.point.position.x() - 10,
                          self.point.position.y() + 20)
            line1.setPen(displacementConstrain.pen)
            line2 = QGraphicsLineItem()
            line2.setLine(self.point.position.x(), self.point.position.y(), self.point.position.x() + 10,
                          self.point.position.y() + 20)
            line2.setPen(displacementConstrain.pen)
            self.addToGroup(line1)
            self.addToGroup(line2)
            line3 = QGraphicsLineItem()
            line3.setLine(line2.line().p2().x(), line2.line().p2().y(), line1.line().p2().x(), line1.line().p2().y())
            line3.setPen(self.pen)
            self.addToGroup(line3)
        if 3 in direction:
            # TODO: implement z rotation
            pass

    def updateConstrain(self, direction):
        pass


class NodalForce(QGraphicsItemGroup):
    def __init__(self, x_value, y_value, position, arrow_size):
        super(NodalForce, self).__init__()
        if x_value != '':
            self.x_value = int(x_value)
        else:
            self.x_value = 0
        if y_value != '':
            self.y_value = int(y_value)
        else:
            self.y_value = 0
        self._create_group(position, arrow_size)

    def _create_group(self, position, arrow_size):
        if self.x_value:
            x = StressRepresentation(position, 180, arrow_size, self.x_value, 'kN')
            self.addToGroup(x)
        if self.y_value:
            y = StressRepresentation(position, 90, arrow_size, self.y_value, 'kN')
            self.addToGroup(y)


class Traction(QGraphicsItemGroup):
    def __init__(self, x_value, y_value, coordinates, positions, angles, arrow_size):
        super(Traction, self).__init__()
        self.coordinates = coordinates
        if x_value != '':
            self.x_value = x_value
        else:
            self.x_value = 0
        if y_value != '':
            self.y_value = y_value
        else:
            self.y_value = 0
        self._create_group(self.x_value, self.y_value, positions, angles, arrow_size)

    def _create_group(self, x_value, y_value, positions, angles, arrow_size):
        if x_value:
            x1 = StressRepresentation(positions[0], angles[0][0], arrow_size, self.x_value, 'MPa')
            self.addToGroup(x1)
            x2 = StressRepresentation(positions[1], angles[1][0], arrow_size, self.x_value, 'MPa')
            self.addToGroup(x2)
        if y_value:
            y1 = StressRepresentation(positions[0], angles[0][1], arrow_size, self.y_value, 'MPa')
            self.addToGroup(y1)
            y2 = StressRepresentation(positions[1], angles[1][1], arrow_size, self.y_value, 'MPa')
            self.addToGroup(y2)

class StressRepresentation(QGraphicsItemGroup):
    pen = QPen(Qt.red, 2)
    def __init__(self, position, angle, arrow_size, value, unit):
        super(StressRepresentation, self).__init__()
        arrow_line = QLineF()
        arrow_line.setP1(position)
        arrow_line.setLength(arrow_size)
        arrow_line.setAngle(angle)
        arrow = QGraphicsLineItem()
        arrow.setLine(arrow_line)
        self.addToGroup(arrow)

        arrow_head1_line = QLineF()
        arrow_head1_line.setP1(arrow_line.p1())
        arrow_head1_line.setLength(arrow_size/4)
        arrow_head1_line.setAngle(arrow_line.angle() + 45)
        arrow_head1 = QGraphicsLineItem()
        arrow_head1.setLine(arrow_head1_line)
        self.addToGroup(arrow_head1)

        arrow_head2_line = QLineF()
        arrow_head2_line.setP1(arrow_line.p1())
        arrow_head2_line.setLength(arrow_size/4)
        arrow_head2_line.setAngle(arrow_line.angle() - 45)
        arrow_head2 = QGraphicsLineItem()
        arrow_head2.setLine(arrow_head2_line)
        self.addToGroup(arrow_head2)

        text = QGraphicsTextItem()
        text.setPlainText(f'{str(value)}{unit}')
        text.setPos(arrow_line.p2())
        self.addToGroup(text)

        self._set_color()

    def _set_color(self):
        for child in self.childItems():
            if type(child) is not QGraphicsTextItem:
                child.setPen(StressRepresentation.pen)
