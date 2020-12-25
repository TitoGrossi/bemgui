import subprocess
import os.path
from itertools import tee

def save_model(file_name, num_points, elements, young, poisson, **kwargs):
    problem_name = file_name.split('/')[-1].split('.')[0]
    with open(f'{file_name}', 'w') as f:
        f.write(f'{problem_name}\n')
        f.write(f'Avaliation mode - todo\n')
        f.write(f'{young}\t{poisson}\n')
        f.write('Nodal_Coordinates_(NODE,X,Y)\n')
        f.write(f'{num_points}\n')
        elements, element_generator = tee(elements)
        f.write(f'{num_points}\n')
        num_elements = 0
        for element in elements:
            f.write(f'{element.initialPoint.idx}\t')
            f.write(f'{round(element.initialPoint.position.x()/1000, 3)}\t')
            f.write(f'{round(-element.initialPoint.position.y()/1000, 3)}\n')
            f.write(f'{element.middlePoint.idx}\t')
            f.write(f'{round(element.middlePoint.position.x()/1000, 3)}\t')
            f.write(f'{round(-element.middlePoint.position.y()/1000, 3)}\n')
            num_elements += 1
        f.write('Mesh_Topology_(ELEMENT,G-NODE1,G-NODE2,G-NODE3)\n')
        f.write(f'{num_elements}\n')
        count = 1
        for element in element_generator:
            # f.write(f'{element.idx}\t') # Print index of element?
            f.write(f'{count}\t')
            f.write(f'{element.initialPoint.idx}\t')
            f.write(f'{element.middlePoint.idx}\t')
            f.write(f'{element.finalPoint.idx}\n')
            count += 1
        f.write('Displacement_Boundary_Conditions_(ELEMENT,L-NODE,G-NODE)\n')

    # BEMCRACKER2D_API(file_name)

def BEMCRACKER2D_API(file):
    '''
    function that calls the executable BEMCRACKER file, parsing in a file as
    argument to extract the numerical results of the model described in it
    '''
    subprocess.Popen(['BEMCRACKER2D', '-f', file])
