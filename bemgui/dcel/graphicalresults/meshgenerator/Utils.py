import bemgui.dcel.meshgenerator.GraphicalElements


def linspace_with_half_point(start, stop, n):
    '''
    returns a linear division of space defined by start, stop into n parts,
    inculding stop and returning also the middle points between those
    '''
    h = (stop - start)/(2*(n - 1))
    for i in range(2*n - 1):
        yield start + h*i

def discontspace_with_half_points(proportions):
    cumulative = 0
    for i in range(len(proportions)):
        yield cumulative
        yield (cumulative + proportions[i])/2
        cumulative = proportions[i]
    yield (cumulative + 1)/2
    yield 1

def generateMeshHelper(half_edge, percentages):
    count = 0
    for percentage_point in percentages:
        if count == 0:
            first_point = bemgui.meshgenerator.GraphicalElements.meshExtremityPoint(half_edge.pointAtPercent(percentage_point), 0)
            count += 1
        elif count == 1:
            middle_point = bemgui.meshgenerator.GraphicalElements.meshMiddlePoint(half_edge.pointAtPercent(percentage_point))
            count += 1
        elif count == 2:
            final_point = bemgui.meshgenerator.GraphicalElements.meshExtremityPoint(half_edge.pointAtPercent(percentage_point), 0)
            element = mesh_element = bemgui.meshgenerator.GraphicalElements.meshElement(first_point, middle_point, final_point)
            first_point = final_point
            yield element
            count = 1
