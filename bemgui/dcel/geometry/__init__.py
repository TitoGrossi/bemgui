'''
Package that describes the classes and methods of the graphical items that are
part of geometry groupbox in the application view. This is specially treated as
a implementation of a doubly-connected edge list, as described in the dutch book,
but it also handles with visibility issues of the items in the scene by keeping
track of items of that type added to the scene with static members of classes
'''

# TODO: Only lacking the arc edges

from bemgui.dcel.geometry import base_elements
from bemgui.dcel.geometry import edges
