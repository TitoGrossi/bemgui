'''
Module containing the MainWindowApp class, which is responsible for holding
information about all the widgets of the application and passing signals to those,
when they are interested in that
'''

from bemgui.resources.uiwindows.mainwindow_ui import Ui_BEMGUI_MainWindow
from bemgui.resources.controler.GraphicsScene import Scene
from bemgui.resources.controler import secondarywindows
from bemgui.resources.controler import informUser
from bemgui.dcel.geometry.base_elements import point, zone
import bemgui.dcel.meshgenerator
import bemgui.dcel.elastostaticanalysis
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindowApp(QtWidgets.QMainWindow, Ui_BEMGUI_MainWindow):
    '''
    Class that applies the logic behind the mainwindow of the application
    '''
    resized = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        #Setting up UI and scene of graphicsView
        super(MainWindowApp, self).__init__(parent)

        self.setupUi(self)
        self.scene = Scene(self)
        self.drawingArea.setScene(self.scene)

        self.xPos = informUser.xPosition(self)
        self.xPos.move(10, 10)
        self.xPos.setProperty('cursor', QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.yPos = informUser.yPosition(self)
        self.yPos.move(self.xPos.pos().x() + 150, 10)
        self.yPos.setProperty('cursor', QtGui.QCursor(QtCore.Qt.IBeamCursor))

        self.status_bar = informUser.status_bar(self)
        self.resized.connect(self.status_bar.update_pos)

        self.undoStack = QtWidgets.QUndoStack()

        #Connecting menu actions to functions
        self.actionDark.triggered.connect(self.changeToDarkPalette)
        self.actionLight.triggered.connect(self.changeToLightPalette)
        self.actionNew.triggered.connect(self.newFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_as.triggered.connect(self.saveFileAs)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)

        #Establishing actions shortcuts
        self.actionNew.setShortcut(QtGui.QKeySequence('Ctrl+N'))
        self.actionSave.setShortcut(QtGui.QKeySequence('Ctrl+S'))
        self.actionSave_as.setShortcut(QtGui.QKeySequence('Ctrl+shift+S'))
        self.actionOpen.setShortcut(QtGui.QKeySequence('Ctrl+O'))
        self.actionUndo.setShortcut(QtGui.QKeySequence('Ctrl+Z'))
        self.actionRedo.setShortcut(QtGui.QKeySequence('Ctrl+Y'))

        #Connecting buttons to functions
        self.createPoints.clicked.connect(lambda: self.setSceneAction('addingPoint'))
        self.createLines.clicked.connect(lambda: self.setSceneAction('drawingLine'))
        self.createArcs.clicked.connect(self.showTypesOfCurvedElementWindow)
        self.defineZones.clicked.connect(lambda: self.setSceneAction('definingZone'))

        self.Run_MESH.clicked.connect(self.generateMesh)

        self.addDisplacement.clicked.connect(self.showDisplacementWindow)
        self.addTraction.clicked.connect(self.showTractionWindow)

        self.runElastosticAnalysis.clicked.connect(self.run_elastostatic_analysis)

    def keyPressEvent(self, event):
        if event.key() == (QtCore.Qt.Key_Control and QtCore.Qt.Key_Q):
            QtWidgets.QApplication.instance().quit()
        elif event.key() == (QtCore.Qt.Key_Control and QtCore.Qt.Key_Escape):
            if self.scene.clicked:
                self.scene.cancel_drawing()
            else:
                self.setSceneAction(None)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(MainWindowApp, self).resizeEvent(event)

    def newFile(self):
        pass

    def saveFile(self):
        pass

    def saveFileAs(self):
        pass

    def openFile(self):
        pass

    def showTypesOfCurvedElementWindow(self):
        result = secondarywindows.elementTypeWindow.getType(self)
        self.setSceneAction(result)

    def showZoneWindow(self, isFirst):
        window = secondarywindows.defineZoneWindow(isFirst)
        return window.getZone(isFirst=isFirst)

    def setSceneAction(self, functionality):
        self.scene.currentAction = functionality

    def generateMesh(self):
        '''
        Generate BEM, FEM or meshless mesh based on geometry of user and user choice
        '''
        if self.BEM_MESH.isChecked():
            self.scene.currentAction = None
            zones = [item for item in self.scene.items() if type(item) is zone]
            mesh = bemgui.dcel.meshgenerator.bemmesh.BEMMesh(self)
            for zn in zones:
                mesh.discretize_zone(zn)
            for item in self.scene.items():
                item.setVisible(False)
            self.scene.setBackgroundBrush(QtCore.Qt.white)
            for zn in zones:
                half_edges = zn.traverse()
                for he in half_edges:
                    for element in he.discretization:
                        self.scene.addItem(element.middlePoint)
                        self.scene.addItem(element.finalPoint)
                        self.scene.addItem(element)
        elif self.FEM_MESH.isChecked():
            pass
        elif self.MESHLESS.isChecked():
            pass
        self.undoStack.clear()

    def getMeshElements(self):
        for element in self.scene.items()[::-1]:
            if type(element) is bemgui.dcel.meshgenerator.GraphicalElements.meshElement:
                yield element

    def run_elastostatic_analysis(self):
        if self.elastostaticStandard.isChecked():
            self.runBEMCRACKER2D()
        elif self.elastostaticNoGrowth.isChecked():
            last_parameters = self.showLastDialogWindow(False)
            self.runBEMCRACKER2D()
        else:
            last_parameters = self.showLastDialogWindow(True)
            self.runBEMCRACKER2D()

    def runBEMCRACKER2D(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Run Elastostatic Analysis',
                                                     '/home/titoalbernaz/Documents/UnB/PF/BEMGUI_project/bemgui/test/test',
                                                     "Text files (*.dat)")
        elements = self.getMeshElements()
        bemgui.dcel.elastostaticanalysis.BEMCRACKER2D_interaction.save_model(name[0], elements)


    def showDiscretionWindow(self, isCrack):
        window = secondarywindows.createDiscretionWindow(isCrack)
        result = window.getDiscretion(isCrack=isCrack)
        return result

    def showTractionWindow(self):
        window = secondarywindows.tractionWindow()
        result = window.getTraction()
        return result

    def showDisplacementWindow(self):
        window = secondarywindows.displacementWindow()
        result = window.getDisplacement()
        return result

    def showConstrainWindow(self):
        pass
        # window = constrainWindow()
        # result = window.getConstrain()
        # return result

    def showLastDialogWindow(self, crackGrowth):
        window = secondarywindows.finalDialogWindow(crackGrowth)
        parameters = window.get_last_parameters(crackGrowth=crackGrowth)
        return parameters

    def undo(self):
        self.undoStack.undo()

    def redo(self):
        self.undoStack.redo()

    def changeToLightPalette(self):
        from bemgui.palettes import light_palette
        self.setPalette(ligth_palette)

    def changeToDarkPalette(self):
        from bemgui.palettes import dark_palette
        self.setPalette(dark_palette)
