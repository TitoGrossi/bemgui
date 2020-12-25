from PyQt5 import QtWidgets
from bemgui.model.geometry.dcel import Zone

def read_file():
    # with open('camtr.dat', 'r') as file:
    #     init_info = file.readline()
    #     num_incr, crack_propagation, num_nodes, num_elements, num_tip = init_info[0], init_info[1:32]

    scene = QtWidgets.QApplication.activeWindow().scene
    zones = [zn for zn in scene.items() if type(zn) is zone]
    points_that_will_grow = set()
    for zn in zones:
        zone_path = zn.traverse()
        for he in zone_path:
            if he.init_point.connectivity == 1:
                points_that_will_grow.add(he.init_point)

    for pnt in points_that_will_grow:
        pass
