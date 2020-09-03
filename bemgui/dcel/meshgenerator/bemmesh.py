from bemgui.dcel.meshgenerator import Utils
from collections import deque
import bemgui.dcel.meshgenerator.GraphicalElements
from bemgui.resources.controler.secondarywindows import createDiscretionWindow


class BEMMesh():
    def __init__(self, parent):
        '''don't really need a class for this, but everything is working fine'''
        self.parent = parent
        self.is_traversing_crack = False
        self.root_point = None

    def discretize_zone(self, zone):
        half_edges = zone.traverse()
        first = True
        for he in half_edges:
            if not first:
                self.discretize_half_edge(he, last_point_from_previous_edge=previous_half_edge.discretization[-1].finalPoint)
            else:
                first_he = he
                self.discretize_half_edge(he)
                first = False
            previous_half_edge = he
        previous_half_edge.discretization[-1].finalPoint = first_he.discretization[0].initialPoint

    def discretize_half_edge(self, he, last_point_from_previous_edge=None):
        if not hasattr(he, 'discretization'):
            if self.is_traversing_crack:
                num, discountinuos = createDiscretionWindow.getDiscretion(he, True, self.parent)
            else:
                num, discountinuos = createDiscretionWindow.getDiscretion(he, False, self.parent)
            elements = []
            if not discountinuos:
                percentages = Utils.linspace_with_half_point(0, 1, num+1)
                for element in Utils.generateMeshHelper(he, percentages, last_point_from_previous_edge):
                    elements.append(element)
            else:
                percentages = bemgui.dcel.meshgenerator.Utils.discontspace_with_half_points(num)
                for element in Utils.generateMeshHelper(he, percentages, last_point_from_previous_edge):
                    elements.append(element)
            reversed_elements = []
            for element in elements[::-1]:
                reversed_element = bemgui.dcel.meshgenerator.GraphicalElements.meshElement(element.finalPoint, element.middlePoint, element.initialPoint)
                reversed_elements.append(reversed_element)
            setattr(he, 'discretization', elements)
            setattr(he.twin, 'discretization', reversed_elements)
            if len(he.twin.init_point.connectivity) > 2:
                self.root_point = he.twin.init_point
                self.is_traversing_crack = True
        else:
            # If we are traversing a half_edge that has already been discretized,
            # we are dealing with the return of a crack
            if he.twin.init_point is self.root_point:
                self.is_traversing_crack = False
