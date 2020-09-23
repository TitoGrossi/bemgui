import subprocess
import os.path
from itertools import tee

def save_model(file_name, elements, young, poisson, **kwargs):
    problem_name = file_name.split('/')[-1].split('.')[0]
    with open(f'{file_name}', 'w') as f:
        f.write(f'{problem_name}\n')
        f.write(f'Avaliation mode - todo\n')
        f.write(f'{young}\t{poisson}\n')
        f.write('Nodal_Coordinates_(NODE,X,Y)\n')
        elements, element_generator = tee(elements)
        elements, displacement_generator = tee(elements)
        elements, traction_generator = tee(elements)
        elements, constrain_unknown_generator = tee(elements)
        for element in elements:
            f.write(f'{element.initialPoint.idx}\t')
            f.write(f'{round(element.initialPoint.position.x()/1000, 3)}\t')
            f.write(f'{round(-element.initialPoint.position.y()/1000, 3)}\n')
            f.write(f'{element.middlePoint.idx}\t')
            f.write(f'{round(element.middlePoint.position.x()/1000, 3)}\t')
            f.write(f'{round(-element.middlePoint.position.y()/1000, 3)}\n')
        f.write('Mesh_Topology_(ELEMENT,G-NODE1,G-NODE2,G-NODE3)\n')
        for element in element_generator:
            f.write(f'{element.idx}\t')
            f.write(f'{element.initialPoint.idx}\t')
            f.write(f'{element.middlePoint.idx}\t')
            f.write(f'{element.finalPoint.idx}\n')
        f.write('Displacement_Boundary_Conditions_(ELEMENT,L-NODE,G-NODE)\n')
        # From here, I need to ask Alvaro and Gil how to display the information!!!
        # for element in traction_generator:
        #     if 1 in element.initialPoint.getDisplacement():
        #         print(1)
        # f.write('Traction_Boundary_Conditions_(ELEMENT,L-NODE,G-NODE)\n')
        # for element in traction_generator:
        #     pass
        # f.write('Constrained_Unknowns_(ELEMENT,L-NODE,G-NODE)\n')
        # for element in constrain_unknown_generator:
        #     pass
        # f.write('Crack_Propagattion_(Number_OF_Crack-Extension_Increments)\n')
        # for constant in **kwargs:
        #     f.write(f'{constant}\n')
    # BEMCRACKER2D_API(file_name)

def BEMCRACKER2D_API(file):
    '''
    function that calls the executable BEMCRACKER file, parsing in a file as
    argument to extract the numerical results of the model described in it
    '''
    subprocess.Popen(['BEMCRACKER2D', '-f', file])
