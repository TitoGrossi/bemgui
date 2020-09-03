'''
Module that contains classes of the types of edges that may be present on the
scene, and deals with specific characteristics of those (update path and intersect
methods, for example). All classes present here inherit from the base class 'edge',
represented on the baseElements module of this very same package (geometry)
'''

from bemgui.dcel.geometry.base_elements import edge
from PyQt5.QtGui import QPainterPath

class straightEdge(edge):
    '''
    Edge representing a straight path
    '''
    num_points_to_complete = 2
    def __init__(self, initialPoint=None, finalPoint=None):
        super(straightEdge, self).__init__(initialPoint=initialPoint, finalPoint=finalPoint)

    def intersects(self, other_element):
        '''
        Method for checking for intersections with other elements
        '''
        pass

    def update(self, eventPos, point=None):
        path = QPainterPath()
        path.moveTo(self.initialPoint.position)
        path.lineTo(eventPos)
        self.setPath(path)
        if point:
            self.finalPoint = point


class arcEdge(edge):
    '''
    Class to represent arc curves. It inherits from element and has its center
    on centerPoint, which is initialized as None
    '''
    num_points_to_complete = 3
    def __init__(self, initialPoint=None, finalPoint=None):
        super(arcEdge, self).__init__(initialPoint=initialPoint, finalPoint=finalPoint)
        self.centerPoint = None

    def intersects(self, other_element):
        pass

    def update(self, eventPos, fase, point=None):
        # If user is setting the final point
        if fase == 1:
            path = QPainterPath()
            path.moveTo(self.initialPoint)
            path.lineTo(eventPos)
        # If user is finishing the path (setting centerPoint)
        elif fase == 2:
            path = QPainterPath()
            path.moveTo(self.initialPoint)
            path.acrTo(eventPos, self.finalPoint)


class quadraticEdge(edge):
    '''
    Class to represent Bézier curves of first degree (quadratic). It inherits
    from element and has on control points, initializing as None
    '''
    num_points_to_complete = 3
    def __init__(self, initialPoint=None, finalPoint=None):
        super(quadraticEdge, self).__init__(initialPoint=initialPoint, finalPoint=finalPoint)
        self.ctrlPoint = None

    def intersects(self, other_element):
        pass

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


class cubicEdge(edge):
    '''
    Class to represent Bézier curves of second degree (cubic). It inherits
    from element and has two control points, both initializing as None
    '''
    num_points_to_complete = 4
    def __init__(self, initialPoint=None, finalPoint=None):
        super(cubicEdge, self).__init__(initialPoint, finalPoint)
        self.ctrlPoint1 = None
        self.ctrlPoint2 = None

    def intersects(self, other_element):
        pass

    def self_intersects(self):
        '''
        Algorithm to check for self intersections in a Bézier curve as explained
        in 'Calculating the Self-Intersction of Bézier Curves' by Dieter Lasser
        from Technische Hochschule Darmstadt Department of Mathematics, in West
        Germany. We're only interested in if there is a self intersection though
        '''
        # Lines connecting initial point, control points and final point of curve
        # in that order
        line1 = QLineF(self.initialPoint.pos, self.ctrlPoint1.pos)
        line2 = QLineF(self.ctrlPoint1.pos, self.ctrlPoint2.pos)
        line3 = QLineF(self.ctrlPoint2.pos, self.finalPoint.pos)

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
