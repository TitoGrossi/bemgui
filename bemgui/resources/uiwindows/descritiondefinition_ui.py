# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'discretionwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_discretionWindow(object):
    def setupUi(self, discretionWindow):
        discretionWindow.setObjectName("discretionWindow")
        discretionWindow.resize(416, 314)
        self.gridLayout = QtWidgets.QGridLayout(discretionWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_isCrack = QtWidgets.QCheckBox(discretionWindow)
        self.checkBox_isCrack.setMaximumSize(QtCore.QSize(122, 16777215))
        self.checkBox_isCrack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_isCrack.setObjectName("checkBox_isCrack")
        self.gridLayout.addWidget(self.checkBox_isCrack, 0, 0, 1, 1)
        self.groupBox_type_of_discretization = QtWidgets.QGroupBox(discretionWindow)
        self.groupBox_type_of_discretization.setObjectName("groupBox_type_of_discretization")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_type_of_discretization)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_type_of_discretization)
        self.radioButton.setMaximumSize(QtCore.QSize(170, 16777215))
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_type_of_discretization)
        self.radioButton_2.setMaximumSize(QtCore.QSize(182, 16777215))
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.gridLayout.addWidget(self.groupBox_type_of_discretization, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(discretionWindow)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.lineEdit_number_of_elements = QtWidgets.QLineEdit(discretionWindow)
        self.lineEdit_number_of_elements.setMaximumSize(QtCore.QSize(167, 16777215))
        self.lineEdit_number_of_elements.setObjectName("lineEdit_number_of_elements")
        self.gridLayout.addWidget(self.lineEdit_number_of_elements, 2, 1, 1, 1)
        self.groupBox_discontinous_discretion = QtWidgets.QGroupBox(discretionWindow)
        self.groupBox_discontinous_discretion.setEnabled(False)
        self.groupBox_discontinous_discretion.setObjectName("groupBox_discontinous_discretion")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_discontinous_discretion)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout.addWidget(self.groupBox_discontinous_discretion, 3, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(164, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(discretionWindow)
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 1, 1, 1)

        self.retranslateUi(discretionWindow)
        self.buttonBox.accepted.connect(discretionWindow.accept)
        self.buttonBox.rejected.connect(discretionWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(discretionWindow)

    def retranslateUi(self, discretionWindow):
        _translate = QtCore.QCoreApplication.translate
        discretionWindow.setWindowTitle(_translate("discretionWindow", "Dialog"))
        self.checkBox_isCrack.setText(_translate("discretionWindow", "Element is Crack"))
        self.groupBox_type_of_discretization.setTitle(_translate("discretionWindow", "Type of discretization"))
        self.radioButton.setText(_translate("discretionWindow", "Continuous discretization"))
        self.radioButton_2.setText(_translate("discretionWindow", "Discontinuous discretization"))
        self.label.setText(_translate("discretionWindow", "Number of elements in discretion:"))
        self.lineEdit_number_of_elements.setPlaceholderText(_translate("discretionWindow", "Enter the number of elements (ex.: 5)"))
        self.groupBox_discontinous_discretion.setTitle(_translate("discretionWindow", "Discontinous discretization box"))
