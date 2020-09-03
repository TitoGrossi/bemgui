# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choosecurvedelementtype.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChooseCurvedElementType(object):
    def setupUi(self, ChooseCurvedElementType):
        ChooseCurvedElementType.setObjectName("ChooseCurvedElementType")
        ChooseCurvedElementType.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(ChooseCurvedElementType)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(ChooseCurvedElementType)
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(ChooseCurvedElementType)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setMaximumSize(QtCore.QSize(240, 16777215))
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setMaximumSize(QtCore.QSize(270, 16777215))
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setMaximumSize(QtCore.QSize(246, 16777215))
        self.radioButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.retranslateUi(ChooseCurvedElementType)
        self.buttonBox.accepted.connect(ChooseCurvedElementType.accept)
        self.buttonBox.rejected.connect(ChooseCurvedElementType.reject)
        QtCore.QMetaObject.connectSlotsByName(ChooseCurvedElementType)

    def retranslateUi(self, ChooseCurvedElementType):
        _translate = QtCore.QCoreApplication.translate
        ChooseCurvedElementType.setWindowTitle(_translate("ChooseCurvedElementType", "Element Type Window"))
        self.groupBox.setTitle(_translate("ChooseCurvedElementType", "Choose the type of element you want to add"))
        self.radioButton.setText(_translate("ChooseCurvedElementType", "Arc Element (contains 3 base points)"))
        self.radioButton_2.setText(_translate("ChooseCurvedElementType", "Quadratic Element (contains 3 base points)"))
        self.radioButton_3.setText(_translate("ChooseCurvedElementType", "Cubic Element (contains 4 base points)"))
