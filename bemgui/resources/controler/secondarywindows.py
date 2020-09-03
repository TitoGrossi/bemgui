from PyQt5.QtWidgets import QDialog, QLineEdit, QGraphicsPathItem
from PyQt5.QtGui import QDoubleValidator, QPen
from PyQt5.QtCore import Qt
from bemgui.resources import uiwindows

class elementTypeWindow(uiwindows.choosecurve_ui.Ui_ChooseCurvedElementType, QDialog):
    def __init__(self, parent=None):
        super(elementTypeWindow, self).__init__(parent)
        self.setupUi(self)
        self.radioButton_2.setChecked(True)
        self.radioButton.setEnabled(False)

    @staticmethod
    def getType(parent=None):
        dialog = elementTypeWindow(parent)
        dialog.exec_()
        if dialog.radioButton.isChecked():
            return 'drawingArc'
        elif dialog.radioButton_2.isChecked():
            return 'drawingQuadratic'
        elif dialog.radioButton_3.isChecked():
            return 'drawingCubic'


class defineZoneWindow(uiwindows.zonedefinition_ui.Ui_DefineZone, QDialog):
    def __init__(self, isFirst, parent=None):
        super(defineZoneWindow, self).__init__(parent)
        self.setupUi(self)
        self.radioButton_2.clicked.connect(self.isHole)
        self.radioButton.clicked.connect(self.isNotHole)
        self.radioButton_3.clicked.connect(self.isNotHole)
        self.isFirst = isFirst
        if self.isFirst:
            self.radioButton_2.setEnabled(False)
            self.radioButton_3.setEnabled(False)
            self.clockwise.setChecked(True)
        else:
            self.radioButton.setEnabled(False)
            self.radioButton_2.setChecked(True)
            self.groupBox_orientation.setEnabled(False)
            self.isHole()

    def isHole(self):
        if not self.radioButton_2.isDown():
            self.lineEdit.setText("0")
            self.lineEdit.setReadOnly(True)
            self.lineEdit_2.setText("0")
            self.lineEdit_2.setReadOnly(True)
            self.counterclockwise.setChecked(True)

    def isNotHole(self):
        self.lineEdit.setText("69")
        self.lineEdit.setReadOnly(False)
        self.lineEdit_2.setText("0.33")
        self.lineEdit_2.setReadOnly(False)
        self.clockwise.setChecked(True)

    @staticmethod
    def getZone(parent=None, isFirst=True):
        dialog = defineZoneWindow(isFirst)
        dialog.exec_()
        elasticity = float(dialog.lineEdit.text())
        poisson = float(dialog.lineEdit_2.text())
        if dialog.radioButton.isChecked():
            type = 1
        elif dialog.radioButton_2.isChecked():
            type = 2
        else:
            type = 3
        return type, elasticity, poisson, int(dialog.clockwise.isChecked())



class createDiscretionWindow(uiwindows.descritiondefinition_ui.Ui_discretionWindow, QDialog):
    def __init__(self, isCrack, he, parent=None):
        # self.parent = parent
        super(createDiscretionWindow, self).__init__(parent)
        self.highlight = QGraphicsPathItem()
        self.highlight.setPath(he)
        pen = QPen(Qt.red, 2)
        self.highlight.setPen(pen)
        self.highlight.setZValue(1)
        self.parent().scene.addItem(self.highlight)
        self.setupUi(self)
        self.move(1450, -1)
        self.isCrack = isCrack
        self.lineEdit_number_of_elements.setFocus(True)
        self.lineEdit_number_of_elements.textChanged.connect(self.change_number_of_discontinous_elements)
        self.radioButton_2.toggled.connect(self.setDiscontinousBoxState)
        if self.isCrack == True:
            self.checkBox_isCrack.setChecked(True)
            self.radioButton_2.setChecked(True)
            self.checkBox_isCrack.setEnabled(False)
            self.groupBox_type_of_discretization.setEnabled(False)

    def setDiscontinousBoxState(self):
        newState = not self.groupBox_discontinous_discretion.isEnabled()
        self.groupBox_discontinous_discretion.setEnabled(newState)

    def change_number_of_discontinous_elements(self):
        if self.radioButton_2.isChecked():
            if self.lineEdit_number_of_elements.text() != "":
                if int(self.lineEdit_number_of_elements.text()) > self.verticalLayout_2.count():
                    for i in range(int(self.lineEdit_number_of_elements.text()) - self.verticalLayout_2.count()):
                        lineEdit = QLineEdit()
                        validator = QDoubleValidator()
                        validator.setNotation(0)
                        validator.setRange(0.1, 0.9, decimals=3)
                        lineEdit.setValidator(validator)
                        self.verticalLayout_2.addWidget(lineEdit)
                else:
                    for i in range(self.verticalLayout_2.count()-1, int(self.lineEdit_number_of_elements.text())-1, -1):
                        itemToDelete = self.verticalLayout_2.itemAt(i).widget()
                        self.verticalLayout_2.removeWidget(itemToDelete)
                        itemToDelete.deleteLater()
            else:
                pass

    @staticmethod
    def getDiscretion(he, isCrack=False, parent=None):
        dialog = createDiscretionWindow(isCrack, he, parent)
        dialog.exec_()
        if dialog.radioButton.isChecked():
            dialog.parent().scene.removeItem(dialog.highlight)
            if dialog.lineEdit_number_of_elements.text() != "":
                return int(dialog.lineEdit_number_of_elements.text()), False
            else:
                return 1, False
        else:
            spaces = [0]
            for i in range(dialog.verticalLayout_2.count()):
                spaces.append(float(dialog.verticalLayout_2.itemAt(i).widget().text()) + spaces[-1])
            dialog.parent().scene.removeItem(dialog.highlight)
            return spaces, True

class displacementWindow(uiwindows.adddisplacement_ui.Ui_setDisplacementCondition, QDialog):
    def __init__(self, parent=None):
        super(displacementWindow, self).__init__(parent)
        self.setupUi(self)

    @staticmethod
    def getDisplacement(parent=None):
        dialog = displacementWindow()
        dialog.exec_()
        return dialog.checkBox.isChecked(), dialog.checkBox_2.isChecked(), dialog.checkBox_3.isChecked()


class tractionWindow(uiwindows.traction_ui.Ui_setModuleOfTraction, QDialog):
    def __init__(self, parent=None):
        super(tractionWindow, self).__init__(parent)
        self.setupUi(self)

    @staticmethod
    def getTraction(parent=None):
        dialog = tractionWindow(parent)
        dialog.exec_()
        return dialog.lineEdit.text()

class finalDialogWindow(uiwindows.processor_ui.Ui_FinalCrackDialog, QDialog):
    def __init__(self, crackGrowth, parent=None):
        super(finalDialogWindow, self).__init__(parent)
        self.setupUi(self)
        self.crackGrowth = crackGrowth
        if not self.crackGrowth:
            self.groupBox.setEnabled(False)
            self.groupBox_2.setEnabled(False)

    @staticmethod
    def get_last_parameters(parent=None, crackGrowth=False):
        dialog = finalDialogWindow(crackGrowth)
        dialog.exec_()
        return dialog.lineEdit.text()
