from PyQt5.QtWidgets import QDialog, QLineEdit, QGraphicsPathItem
from PyQt5.QtGui import QDoubleValidator, QPen
from PyQt5.QtCore import Qt
from bemgui.resources import uiwindows

class elementTypeWindow(uiwindows.choosecurve_ui.Ui_ChooseCurvedElementType, QDialog):
    def __init__(self, parent=None):
        super(elementTypeWindow, self).__init__(parent)
        self.setupUi(self)
        self.radioButton.setChecked(True)

    @classmethod
    def getType(cls, parent=None):
        dialog = cls(parent)
        dialog.exec_()
        if dialog.radioButton.isChecked():
            return 'drawingArc'
        elif dialog.radioButton_2.isChecked():
            return 'drawingQuadratic'
        elif dialog.radioButton_3.isChecked():
            return 'drawingCubic'


class defineZoneWindow(uiwindows.zonedefinition_ui.Ui_DefineZone, QDialog):
    def __init__(self, parent, isFirst):
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

    @classmethod
    def getZone(cls, parent, isFirst):
        dialog = cls(parent, isFirst)
        dialog.exec_()
        elasticity = float(dialog.lineEdit.text())
        poisson = float(dialog.lineEdit_2.text())
        if dialog.radioButton.isChecked():
            type = 1
        elif dialog.radioButton_2.isChecked():
            type = 2
        else:
            type = 3
        return type, elasticity, poisson, dialog.clockwise.isChecked()



class createDiscretionWindow(uiwindows.descritiondefinition_ui.Ui_discretionWindow, QDialog):
    def __init__(self, isCrack, he, parent=None):
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

    @classmethod
    def getDiscretion(cls, he, isCrack=False, parent=None):
        dialog = cls(isCrack, he, parent)
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

    @classmethod
    def getDisplacement(cls, parent=None):
        dialog = displacementWindow(parent)
        dialog.exec_()
        restr_and_disp = {1: {}, 2: {}}
        if dialog.checkBox_initial_x.isChecked():
            if dialog.lineEdit_initial_x.text() != "":
                restr_and_disp[1]['x'] = int(dialog.lineEdit_initial_x.text())
            else:
                restr_and_disp[1]['x'] = 0
        if dialog.checkBox_initial_y.isChecked():
            if dialog.lineEdit_initial_y.text() != "":
                restr_and_disp[1]['y'] = int(dialog.lineEdit_initial_y.text())
            else:
                restr_and_disp[1]['y'] = 0
        if dialog.checkBox_initial_z.isChecked():
            if dialog.lineEdit_initial_z.text() != "":
                restr_and_disp[1]['z'] = int(dialog.lineEdit_initial_z.text())
            else:
                restr_and_disp[1]['z'] = 0
        if dialog.checkBox_middle_x.isChecked():
            if dialog.lineEdit_middle_x.text() != "":
                restr_and_disp[2]['x'] = int(dialog.lineEdit_middle_x.text())
            else:
                restr_and_disp[2]['x'] = 0
        if dialog.checkBox_middle_y.isChecked():
            if dialog.lineEdit_middle_y.text() != "":
                restr_and_disp[2]['y'] = int(dialog.lineEdit_middle_y.text())
            else:
                restr_and_disp[2]['y'] = 0
        if dialog.checkBox_middle_z.isChecked():
            if dialog.lineEdit_middle_z.text() != "":
                restr_and_disp[2]['z'] = int(dialog.lineEdit_middle_z.text())
            else:
                restr_and_disp[2]['z'] = 0
        return restr_and_disp


class tractionWindow(uiwindows.addtraction_ui.Ui_setModuleOfTraction, QDialog):
    def __init__(self, parent=None):
        super(tractionWindow, self).__init__(parent)
        self.setupUi(self)

    def addTractionToSelectedItems(self):
        if self.lineEdit_module_element.text() != '':
            for selectedItem in self.parent().scene.selectedItems():
                print(1)

    @classmethod
    def getTraction(cls, parent=None):
        dialog = tractionWindow(parent)
        dialog.exec_()
        dialog.addTractionToSelectedItems()
        return 1
        # return dialog.lineEdit.text()

class finalDialogWindow(uiwindows.processor_ui.Ui_FinalCrackDialog, QDialog):
    def __init__(self, parent, crackGrowth):
        super(finalDialogWindow, self).__init__(parent)
        self.setupUi(self)
        self.crackGrowth = crackGrowth
        if not self.crackGrowth:
            self.groupBox.setEnabled(False)
            self.groupBox_2.setEnabled(False)
        self.buttonBox.accepted.connect(self.parent().runBEMCRACKER2D)

    @classmethod
    def get_last_parameters(cls,parent=None, crackGrowth=False):
        dialog = finalDialogWindow(parent, crackGrowth)
        dialog.exec_()
        inc_num = dialog.lineEdit.text()
        inc_size = dialog.lineEdit_2.text()
        paris_C = dialog.lineEdit_3.text()
        paris_m = dialog.lineEdit_4.text()
        paris_stress_ratio = dialog.lineEdit_5.text()
        increase_number = dialog.lineEdit_6.text()
        return inc_num, inc_size, paris_C, paris_m, paris_stress_ratio, increase_number
