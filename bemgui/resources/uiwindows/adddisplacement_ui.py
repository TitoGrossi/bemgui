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
        setDisplacementCondition.resize(338, 220)
        self.gridLayout = QtWidgets.QGridLayout(setDisplacementCondition)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(setDisplacementCondition)
        self.checkBox.setMaximumSize(QtCore.QSize(216, 16777215))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(setDisplacementCondition)
        self.checkBox_2.setMaximumSize(QtCore.QSize(204, 16777215))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(setDisplacementCondition)
        self.checkBox_3.setMaximumSize(QtCore.QSize(129, 16777215))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(setDisplacementCondition)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.retranslateUi(setDisplacementCondition)
        self.buttonBox.accepted.connect(setDisplacementCondition.accept)
        self.buttonBox.rejected.connect(setDisplacementCondition.reject)
        QtCore.QMetaObject.connectSlotsByName(setDisplacementCondition)

    def retranslateUi(self, setDisplacementCondition):
        _translate = QtCore.QCoreApplication.translate
        setDisplacementCondition.setWindowTitle(_translate("setDisplacementCondition", "Displacement window"))
        self.checkBox.setText(_translate("setDisplacementCondition", "Horizontal displacement constrain"))
        self.checkBox_2.setText(_translate("setDisplacementCondition", "Vertical displacement constrain"))
        self.checkBox_3.setText(_translate("setDisplacementCondition", "Rotation constrain"))
