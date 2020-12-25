from bemgui.model.meshgenerator import utils
from collections import deque
import bemgui.model.meshgenerator.graphical_elements
from bemgui.controller.secondarywindows import createDiscretionWindow


class BEMMesh():
    def __init__(self, parent):
        self.parent = parent
        self.is_traversing_crack = False
        self.root_point = None
        self.crack_forks = []

    def discretize_zone(self, zone):
        half_edges = zone.traverse_outer()
        first = True
        for he in half_edges:
            if not first:
                self.discretize_half_edge(he, last_point_from_previous_edge=previous_half_edge.discretization[-1].finalPoint)
            else:
                first_he = he
                self.discretize_half_edge(he)
                first = False
            previous_half_edge = he
        last_point = previous_half_edge.discretization[-1].finalPoint
        previous_half_edge.discretization[-1].finalPoint = first_he.discretization[0].initialPoint
        last_point.__del__()

    def discretize_half_edge(self, he, last_point_from_previous_edge=None):
        if not hasattr(he, 'discretization'):
            if self.is_traversing_crack:
                num, discountinuos = createDiscretionWindow.getDiscretion(he, True, self.parent)
            else:
                num, discountinuos = createDiscretionWindow.getDiscretion(he, False, self.parent)
            elements = []
            if not discountinuos:
                percentages = utils.linspace_with_half_point(0, 1, num+1)
                for element in utils.generateMeshHelper(he, percentages, last_point_from_previous_edge):
                    elements.append(element)
            else:
                percentages = bemgui.model.meshgenerator.utils.discontspace_with_half_points(num)
                for element in utils.generateMeshHelper(he, percentages, last_point_from_previous_edge):
                    elements.append(element)
            reversed_elements = []
            for element in elements[::-1]:
                reversed_element = bemgui.model.meshgenerator.graphical_elements.meshElement(element.finalPoint, element.middlePoint, element.initialPoint)
                reversed_elements.append(reversed_element)
            setattr(he, 'discretization', elements)
            setattr(he.twin, 'discretization', reversed_elements)
            if not self.is_traversing_crack:
                if len(he.twin.init_point.connectivity) > 2 or len(he.twin.init_point.connectivity) == 2 and he.init_point is he.twin.init_point:
                    if he.twin.previous.twin.left is he.left:
                        self.root_point = he.twin.init_point
                        self.is_traversing_crack = True
                        for fork in he.twin.init_point.connectivity:
                            if fork.half_edge is not he and fork.half_edge.twin is not he:
                                if fork.half_edge.init_point is self.root_point:
                                    self.crack_forks.append(fork.half_edge)
                                else:
                                    self.crack_forks.append(fork.half_edge.twin)
        else:
            # If we are traversing a half_edge that has already been discretized,
            # we are dealing with the return of a crack
            if he.twin.init_point is self.root_point:
                self.crack_forks.remove(he.twin)
            if len(self.crack_forks) == 1:
                self.is_traversing_crack = False
                self.crack_forks = []
