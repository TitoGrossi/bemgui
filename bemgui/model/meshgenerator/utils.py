import bemgui.model.meshgenerator.graphical_elements


def linspace_with_half_point(start, stop, n):
    '''
    returns a linear division of space defined by start, stop into n parts,
    inculding stop and returning also the middle points between those
    '''
    h = (stop - start)/(2*(n - 1))
    for i in range(2*n - 1):
        yield start + h*i

def discontspace_with_half_points(proportions):
    cumulative = proportions[0]
    for i in range(len(proportions)-1):
        yield proportions[i]
        yield (proportions[i]+proportions[i+1])/2
    yield 1

def generateMeshHelper(half_edge, percentages, last_point_from_previous_edge=None):
    count = 0
    for percentage_point in percentages:
        if count == 0:
            if last_point_from_previous_edge:
                first_point = last_point_from_previous_edge
            else:
                first_point = bemgui.model.meshgenerator.graphical_elements.meshExtremityPoint(half_edge.pointAtPercent(percentage_point), 0)
            count += 1
        elif count == 1:
            middle_point = bemgui.model.meshgenerator.graphical_elements.meshMiddlePoint(half_edge.pointAtPercent(percentage_point))
            count += 1
        elif count == 2:
            final_point = bemgui.model.meshgenerator.graphical_elements.meshExtremityPoint(half_edge.pointAtPercent(percentage_point), 0)
            element = mesh_element = bemgui.model.meshgenerator.graphical_elements.meshElement(first_point, middle_point, final_point)
            first_point = final_point
            yield element
            count = 1
