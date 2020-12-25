import subprocess
import os.path
from itertools import tee

from PyQt5.QtWidgets import QFileDialog
import os.path, getpass

def save_model(parent_window):
    userName = getpass.getuser()
    fileName = QFileDialog.getSaveFileName(parent_window, 'Run Analisys',
                                   f'/home/{userName}/untitled.dat',
                                   'Text (*.dat)')
    return fileName

def BEMCRACKER2D_API(parent_window, zones):
    '''
    function that calls the executable BEMCRACKER file, parsing in a file as
    argument to extract the numerical results of the model described in it
    '''
    file_name, extension = save_model(parent_window)
    if file_name != '':
        file_writer = fileWriter(file_name, zones)
        file_writer.writeModelOnFile()
        # subprocess.Popen(['BEMCRACKER2D', '-f', file])


class zoneDescriptior():
    def __init__(self, zn, file):
        self.zn = zn
        self.nodes = set()
        self.file = file

    def writeZoneInformationOnFile(self):
        elements = self.getElementsInOrder()
        self.writeIntialInfoZone(len(elements))
        self.writeMeshTopologyOnFile(elements)

    def getElementsInOrder(self):
        edges = self.zn.traverse()
        elements = []
        for edge in edges:
            for element in edge.discretization:
                elements.append(element)
        return elements

    def writeIntialInfoZone(self, num_elements):
        self.file.write(f'Mesh_Topology_(ELEMENT,G-NODE1,G-NODE2,G-NODE3)_{self.zn}\n')
        self.file.write(f'{self.zn.youngModule} {self.zn.poissonCoeficient} {num_elements}\n')

    def writeMeshTopologyOnFile(self, elements):
        for element in elements:
            self.file.write(f'{element.idx} {element.initialPoint.idx} {element.middlePoint.idx} {element.finalPoint.idx}\n')
            # if 1 in element.finalPoint.restrictions:
                #


class fileWriter():
    def __init__(self, file_name, zones, *args):
        self.file_name = file_name
        self.zones = zones

    def writeModelOnFile(self):
        with open(self.file_name, 'w') as f:
            self.writeInitialInformation(f)
            self.writeNodesCoordsOnFile(f)
            self.writeZonesOnFile(f)

    def writeNodesCoordsOnFile(self, f):
        nodes = set()
        num_zones = 0
        self.zones, zones_copy = tee(self.zones)
        for zone in zones_copy:
            num_zones += 1
            for edge in zone.traverse():
                for element in edge.discretization:
                    nodes.add(element.initialPoint)
                    nodes.add(element.finalPoint)
        f.write(f'{len(nodes)} ')
        f.write(f'{num_zones}\n')
        f.write('Nodal_Coordinates_(NODE,X,Y)\n')
        for node in nodes:
            f.write(f'{node.idx} {node.position.x()} {node.position.y()}\n')

    def writeZonesOnFile(self, f):
        for zn in self.zones:
            zone_description = zoneDescriptior(zn, f)
            zone_description.writeZoneInformationOnFile()

    def writeInitialInformation(self, f):
        problem_name = self.file_name.split('/')[-1].split('.')[0]
        f.write(f'{problem_name}\n')
        f.write(f'Avaliation mode - todo\n')

    def writeFinalInformations(self, f, elements, *args):
        f.write('Crack_Propagattion_(Number_OF_Crack-Extension_Increments)\n')
        for constant in args:
            f.write(f'{constant}\n')
