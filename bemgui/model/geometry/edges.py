'''
Module that contains classes of the types of edges that may be present on the
scene, and deals with specific characteristics of those (update path and intersect
methods, for example). All classes present here inherit from the base class 'edge',
represented on the baseElements module of this very same package (geometry)
'''

from bemgui.model.geometry.dcel import Edge
from PyQt5.QtGui import QPainterPath
from PyQt5.QtCore import QRectF, QLineF

class straightEdge(Edge):
    '''
    Edge representing a straight path
    '''
    num_points_to_complete = 2
    def __init__(self, initialPoint=None, finalPoint=None):
        super(straightEdge, self).__init__(initialPoint=initialPoint, finalPoint=finalPoint)

    def shape(self):
        if self.finalPoint:
            path = QPainterPath()
            path.moveTo(self.path().pointAtPercent(4/self.path().length()))
            path.lineTo(self.path().pointAtPercent(1 - 4/self.path().length()))
            path.lineTo(self.path().pointAtPercent(4/self.path().length()))
            return path
        else:
            return super(straightEdge, self).shape()

    def update(self, eventPos, point=None):
        path = QPainterPath()
        path.moveTo(self.initialPoint.position)
        path.lineTo(eventPos)
        self.setPath(path)
        if point:
            self.finalPoint = point


class arcEdge(Edge):
    '''
    Class to represent arc curves. It inherits from element and has its center
    on centerPoint, which is initialized as None
    '''
    num_points_to_complete = 3
    def __init__(self, initialPoint=None, finalPoint=None):
        super(arcEdge, self).__init__(initialPoint=initialPoint, finalPoint=finalPoint)
        self.centerPoint = None

    def shape(self):
        # print(2)
        if self.centerPoint:
            r = ((self.centerPoint.x() - self.initialPoint.position.x())**2 + (self.centerPoint.y() - self.initialPoint.position.y())**2)**(1/2)
            w, h = 2*r, 2*r
            pf = self.path().pointAtPercent(1 - 4/self.path().length())
            pi = self.path().pointAtPercent(4/self.path().length())
            line1 = QLineF(self.centerPoint.position, pi)
            line2 = QLineF(self.centerPoint.position, pf)
            startAngle, arcLength = line1.angle(), -(line1.angle() - line2.angle())
            if arcLength == 0:
                arcLength = 360
            path = QPainterPath()
            path.moveTo(pi)
            path.arcTo(self.path().boundingRect(), startAngle, arcLength)
            path.arcTo(self.path().boundingRect(), line2.angle(), -arcLength)
            return path
        else:
            return super(arcEdge, self).shape()

    def update(self, eventPos, fase, point=None):
        # If user is setting the final point
        if fase == 1:
            if fase == 1:
                path = QPainterPath()
                path.moveTo(self.initialPoint.position)
                path.lineTo(eventPos)
                self.setPath(path)
                if point:
                    self.finalPoint = point
        # If user is finishing the path (setting centerPoint)
        elif fase == 2:
            path = QPainterPath()
            path.moveTo(self.initialPoint.position)
            r = ((eventPos.x() - self.initialPoint.position.x())**2 + (eventPos.y() - self.initialPoint.position.y())**2)**(1/2)
            x, y, w, h = eventPos.x() - r, eventPos.y() - r, 2*r, 2*r
            line1 = QLineF(eventPos, self.initialPoint.position)
            line2 = QLineF(eventPos, self.finalPoint.position)
            startAngle, arcLenghth = line1.angle(), -(line1.angle() - line2.angle())
            if arcLenghth == 0:
                arcLenghth = 360
            path.arcTo(x, y, w, h, startAngle, arcLenghth)
            self.setPath(path)
            if point:
                self.centerPoint = point


class quadraticEdge(Edge):
    '''
    Class to represent Bézier curves of first degree (quadratic). It inherits
    from element and has on control points, initializing as None
    '''
    num_points_to_complete = 3
    def __init__(self, initialPoint=None, finalPoint=None):
        super(quadraticEdge, self).__init__(initialPoint=initialPoint, finalPoint=finalPoint)
        self.ctrlPoint = None

    def shape(self):
        if self.ctrlPoint:
            path = QPainterPath()
            path.moveTo(self.path().pointAtPercent(4/self.path().length()).x(), self.path().pointAtPercent(4/self.path().length()).y())
            path.quadTo(self.ctrlPoint.position.x(), self.ctrlPoint.position.y(), self.path().pointAtPercent(1 - 4/self.path().length()).x(), self.path().pointAtPercent(1 - 4/self.path().length()).y())
            path.quadTo(self.ctrlPoint.position.x(), self.ctrlPoint.position.y(), self.path().pointAtPercent(4/self.path().length()).x(), self.path().pointAtPercent(4/self.path().length()).y())
            return path
        else:
            return super(quadraticEdge, self).shape()

    def update(self, eventPos, fase, point=None):
        # If user is setting the final point
        if fase == 1:
            path = QPainterPath()
            path.moveTo(self.initialPoint.position)
            path.lineTo(eventPos)
            self.setPath(path)
            if point:
                self.finalPoint = point
        # If user is finishing the path (setting ctrlPoint)
        elif fase == 2:
            path = QPainterPath()
            path.moveTo(self.initialPoint.position)
            path.quadTo(eventPos, self.finalPoint.position)
            self.setPath(path)
            if point:
                self.ctrlPoint = point


class cubicEdge(Edge):
    '''
    Class to represent Bézier curves of second degree (cubic). It inherits
    from element and has two control points, both initializing as None
    '''
    num_points_to_complete = 4
    def __init__(self, initialPoint=None, finalPoint=None):
        super(cubicEdge, self).__init__(initialPoint, finalPoint)
        self.ctrlPoint1 = None
        self.ctrlPoint2 = None

    def shape(self):
        if self.ctrlPoint2:
            path = QPainterPath()
            path.moveTo(self.path().pointAtPercent(4/self.path().length()).x(), self.path().pointAtPercent(4/self.path().length()).y())
            path.cubicTo(self.ctrlPoint1.position.x(), self.ctrlPoint1.position.y(), self.ctrlPoint2.position.x(), self.ctrlPoint2.position.y(), self.path().pointAtPercent(1 - 4/self.path().length()).x(), self.path().pointAtPercent(1 - 4/self.path().length()).y())
            path.cubicTo(self.ctrlPoint2.position.x(), self.ctrlPoint2.position.y(), self.ctrlPoint1.position.x(), self.ctrlPoint1.position.y(), self.path().pointAtPercent(4/self.path().length()).x(), self.path().pointAtPercent(4/self.path().length()).y())
            return path
        else:
            return super(cubicEdge, self).shape()

    def self_intersects(self):
        '''
        Algorithm to check for self intersections in a Bézier curve as explained
        in 'Calculating the Self-Intersction of Bézier Curves' by Dieter Lasser
        from Technische Hochschule Darmstadt Department of Mathematics, in West
        Germany. We're only interested in if there is a self intersection though
        '''
        # Lines connecting initial point, control points and final point of curve
        # in that order
        line1 = QLineF(self.initialPoint.position, self.ctrlPoint1.position)
        line2 = QLineF(self.ctrlPoint1.position, self.ctrlPoint2.position)
        line3 = QLineF(self.ctrlPoint2.position, self.finalPoint.position)

        # Angles between the 3 lines
        angle1 = line1.angleTo(line2) # Positive angle between the first two lines
        # Fixing the sine for the first angle
        if line1.angle() < line2.angle():
            angle1 *= -1
        angle2 = line2.angleTo(line3) # Positive angle between the last two lines
        # Fixing the sine for the second angle
        if line2.angle() < line3.angle():
            angle2 *= -1

        # If the angles sum up to 180 degrees or greater, there is a self-intersection
        if abs(angle1 + angle2) > 180:
            return True
        # Othewise, there is no self intersection
        return False

    def update(self, eventPos, fase, point=None):
        # If user is setting the final point
        if fase == 1:
            path = QPainterPath()
            path.moveTo(self.initialPoint.position)
            path.lineTo(eventPos)
            self.setPath(path)
            if point:
                self.finalPoint = point
        # If user is setting ctrlPoint1
        elif fase == 2:
            path = QPainterPath()
            path.moveTo(self.initialPoint.position)
            path.quadTo(eventPos, self.finalPoint.position)
            self.setPath(path)
            if point:
                self.ctrlPoint1 = point
        # If user is finishing the path (setting ctrlPoint2)
        elif fase == 3:
            path = QPainterPath()
            path.moveTo(self.initialPoint.position)
            path.cubicTo(self.ctrlPoint1.position, eventPos, self.finalPoint.position)
            self.setPath(path)
            if point:
                self.ctrlPoint2 = point
