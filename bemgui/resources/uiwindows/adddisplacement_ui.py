# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setdisplacementcondition.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_setDisplacementCondition(object):
    def setupUi(self, setDisplacementCondition):
        setDisplacementCondition.setObjectName("setDisplacementCondition")
        setDisplacementCondition.resize(234, 331)
        setDisplacementCondition.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.verticalLayout = QtWidgets.QVBoxLayout(setDisplacementCondition)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_initial_point = QtWidgets.QGroupBox(setDisplacementCondition)
        self.groupBox_initial_point.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.groupBox_initial_point.setObjectName("groupBox_initial_point")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_initial_point)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_initial_x = QtWidgets.QLineEdit(self.groupBox_initial_point)
        self.lineEdit_initial_x.setEnabled(False)
        self.lineEdit_initial_x.setObjectName("lineEdit_initial_x")
        self.gridLayout.addWidget(self.lineEdit_initial_x, 0, 1, 1, 1)
        self.checkBox_initial_x = QtWidgets.QCheckBox(self.groupBox_initial_point)
        self.checkBox_initial_x.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_initial_x.setObjectName("checkBox_initial_x")
        self.gridLayout.addWidget(self.checkBox_initial_x, 0, 0, 1, 1)
        self.checkBox_initial_y = QtWidgets.QCheckBox(self.groupBox_initial_point)
        self.checkBox_initial_y.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_initial_y.setObjectName("checkBox_initial_y")
        self.gridLayout.addWidget(self.checkBox_initial_y, 1, 0, 1, 1)
        self.checkBox_apply_same_all = QtWidgets.QCheckBox(self.groupBox_initial_point)
        self.checkBox_apply_same_all.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_apply_same_all.setObjectName("checkBox_apply_same_all")
        self.gridLayout.addWidget(self.checkBox_apply_same_all, 3, 0, 1, 2)
        self.lineEdit_initial_y = QtWidgets.QLineEdit(self.groupBox_initial_point)
        self.lineEdit_initial_y.setEnabled(False)
        self.lineEdit_initial_y.setObjectName("lineEdit_initial_y")
        self.gridLayout.addWidget(self.lineEdit_initial_y, 1, 1, 1, 1)
        self.lineEdit_initial_z = QtWidgets.QLineEdit(self.groupBox_initial_point)
        self.lineEdit_initial_z.setEnabled(False)
        self.lineEdit_initial_z.setObjectName("lineEdit_initial_z")
        self.gridLayout.addWidget(self.lineEdit_initial_z, 2, 1, 1, 1)
        self.checkBox_initial_z = QtWidgets.QCheckBox(self.groupBox_initial_point)
        self.checkBox_initial_z.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_initial_z.setObjectName("checkBox_initial_z")
        self.gridLayout.addWidget(self.checkBox_initial_z, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_initial_point)
        self.groupBox_middle_point = QtWidgets.QGroupBox(setDisplacementCondition)
        self.groupBox_middle_point.setObjectName("groupBox_middle_point")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_middle_point)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_middle_x = middlePointLineEdit(self.groupBox_middle_point)
        self.lineEdit_middle_x.setEnabled(False)
        self.lineEdit_middle_x.setObjectName("lineEdit_middle_x")
        self.gridLayout_2.addWidget(self.lineEdit_middle_x, 0, 1, 1, 1)
        self.lineEdit_middle_y = middlePointLineEdit(self.groupBox_middle_point)
        self.lineEdit_middle_y.setEnabled(False)
        self.lineEdit_middle_y.setObjectName("lineEdit_middle_y")
        self.gridLayout_2.addWidget(self.lineEdit_middle_y, 1, 1, 1, 1)
        self.checkBox_middle_x = middlePointCheckBox(self.groupBox_middle_point)
        self.checkBox_middle_x.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_middle_x.setObjectName("checkBox_middle_x")
        self.gridLayout_2.addWidget(self.checkBox_middle_x, 0, 0, 1, 1)
        self.checkBox_middle_y = middlePointCheckBox(self.groupBox_middle_point)
        self.checkBox_middle_y.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_middle_y.setObjectName("checkBox_middle_y")
        self.gridLayout_2.addWidget(self.checkBox_middle_y, 1, 0, 1, 1)
        self.checkBox_middle_z = middlePointCheckBox(self.groupBox_middle_point)
        self.checkBox_middle_z.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_middle_z.setObjectName("checkBox_middle_z")
        self.gridLayout_2.addWidget(self.checkBox_middle_z, 2, 0, 1, 1)
        self.lineEdit_middle_z = middlePointLineEdit(self.groupBox_middle_point)
        self.lineEdit_middle_z.setEnabled(False)
        self.lineEdit_middle_z.setObjectName("lineEdit_middle_z")
        self.gridLayout_2.addWidget(self.lineEdit_middle_z, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_middle_point)
        self.buttonBox = QtWidgets.QDialogButtonBox(setDisplacementCondition)
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(setDisplacementCondition)
        self.buttonBox.accepted.connect(setDisplacementCondition.accept)
        self.buttonBox.rejected.connect(setDisplacementCondition.reject)
        self.checkBox_initial_x.toggled['bool'].connect(self.lineEdit_initial_x.setEnabled)
        self.checkBox_initial_y.toggled['bool'].connect(self.lineEdit_initial_y.setEnabled)
        self.checkBox_initial_z.toggled['bool'].connect(self.lineEdit_initial_z.setEnabled)
        self.checkBox_middle_x.toggled['bool'].connect(self.lineEdit_middle_x.setEnabled)
        self.checkBox_middle_y.toggled['bool'].connect(self.lineEdit_middle_y.setEnabled)
        self.checkBox_middle_z.toggled['bool'].connect(self.lineEdit_middle_z.setEnabled)
        self.checkBox_initial_x.clicked.connect(self.lineEdit_initial_x.clear)
        self.checkBox_initial_y.clicked.connect(self.lineEdit_initial_y.clear)
        self.checkBox_initial_z.clicked.connect(self.lineEdit_initial_z.clear)
        self.checkBox_middle_x.clicked.connect(self.lineEdit_middle_x.clear)
        self.checkBox_middle_y.clicked.connect(self.lineEdit_middle_y.clear)
        self.checkBox_middle_z.clicked.connect(self.lineEdit_middle_z.clear)
        self.checkBox_apply_same_all.toggled['bool'].connect(self.groupBox_middle_point.setDisabled)
        self.checkBox_apply_same_all.toggled['bool'].connect(self.copyInfoFromInitial)
        self.checkBox_initial_x.toggled['bool'].connect(self.checkBox_middle_x.toggleIfParentIsDisabled)
        self.checkBox_initial_y.toggled['bool'].connect(self.checkBox_middle_y.toggleIfParentIsDisabled)
        self.checkBox_initial_z.toggled['bool'].connect(self.checkBox_middle_z.toggleIfParentIsDisabled)
        self.lineEdit_initial_x.textChanged['QString'].connect(self.lineEdit_middle_x.updateTextIfParentIsDisabled)
        self.lineEdit_initial_y.textChanged['QString'].connect(self.lineEdit_middle_y.updateTextIfParentIsDisabled)
        self.lineEdit_initial_z.textChanged['QString'].connect(self.lineEdit_middle_z.updateTextIfParentIsDisabled)
        QtCore.QMetaObject.connectSlotsByName(setDisplacementCondition)
        setDisplacementCondition.setTabOrder(self.checkBox_initial_x, self.lineEdit_initial_x)
        setDisplacementCondition.setTabOrder(self.lineEdit_initial_x, self.checkBox_initial_y)
        setDisplacementCondition.setTabOrder(self.checkBox_initial_y, self.lineEdit_initial_y)
        setDisplacementCondition.setTabOrder(self.lineEdit_initial_y, self.checkBox_initial_z)
        setDisplacementCondition.setTabOrder(self.checkBox_initial_z, self.lineEdit_initial_z)
        setDisplacementCondition.setTabOrder(self.lineEdit_initial_z, self.checkBox_apply_same_all)
        setDisplacementCondition.setTabOrder(self.checkBox_apply_same_all, self.checkBox_middle_x)
        setDisplacementCondition.setTabOrder(self.checkBox_middle_x, self.lineEdit_middle_x)
        setDisplacementCondition.setTabOrder(self.lineEdit_middle_x, self.checkBox_middle_y)
        setDisplacementCondition.setTabOrder(self.checkBox_middle_y, self.lineEdit_middle_y)
        setDisplacementCondition.setTabOrder(self.lineEdit_middle_y, self.checkBox_middle_z)
        setDisplacementCondition.setTabOrder(self.checkBox_middle_z, self.lineEdit_middle_z)

    def retranslateUi(self, setDisplacementCondition):
        _translate = QtCore.QCoreApplication.translate
        setDisplacementCondition.setWindowTitle(_translate("setDisplacementCondition", "Add Displacement Restrictions"))
        self.groupBox_initial_point.setTitle(_translate("setDisplacementCondition", "Initial Extremity Point"))
        self.checkBox_initial_x.setText(_translate("setDisplacementCondition", "X (mm)"))
        self.checkBox_initial_y.setText(_translate("setDisplacementCondition", "Y (mm)"))
        self.checkBox_apply_same_all.setText(_translate("setDisplacementCondition", "Repeat for all others"))
        self.checkBox_initial_z.setText(_translate("setDisplacementCondition", "Z (rad)"))
        self.groupBox_middle_point.setTitle(_translate("setDisplacementCondition", "Middle Point"))
        self.checkBox_middle_x.setText(_translate("setDisplacementCondition", "X (mm)"))
        self.checkBox_middle_y.setText(_translate("setDisplacementCondition", "Y (mm)"))
        self.checkBox_middle_z.setText(_translate("setDisplacementCondition", "Z (rad)"))

    def copyInfoFromInitial(self):
        self.checkBox_middle_x.setChecked(self.checkBox_initial_x.isChecked())
        self.checkBox_middle_y.setChecked(self.checkBox_initial_y.isChecked())
        self.checkBox_middle_z.setChecked(self.checkBox_initial_z.isChecked())
        self.lineEdit_middle_x.setText(self.lineEdit_initial_x.text())
        self.lineEdit_middle_y.setText(self.lineEdit_initial_y.text())
        self.lineEdit_middle_z.setText(self.lineEdit_initial_z.text())


class middlePointGroupBox(QtWidgets.QGroupBox):
    def __init__(self, parent):
        pass

class middlePointLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent):
        super(middlePointLineEdit, self).__init__(parent)

    def updateTextIfParentIsDisabled(self, text):
        if not self.parent().isEnabled():
            self.setText(text)


class middlePointCheckBox(QtWidgets.QCheckBox):
    def __init__(self, parent):
        super(middlePointCheckBox, self).__init__(parent)

    def toggleIfParentIsDisabled(self, bool):
        if not self.parent().isEnabled():
            self.setChecked(bool)
