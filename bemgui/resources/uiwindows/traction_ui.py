# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setmoduleoftraction.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_setModuleOfTraction(object):
    def setupUi(self, setModuleOfTraction):
        setModuleOfTraction.setObjectName("setModuleOfTraction")
        setModuleOfTraction.resize(400, 81)
        self.formLayout = QtWidgets.QFormLayout(setModuleOfTraction)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(setModuleOfTraction)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(setModuleOfTraction)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(setModuleOfTraction)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)

        self.retranslateUi(setModuleOfTraction)
        self.buttonBox.accepted.connect(setModuleOfTraction.accept)
        self.buttonBox.rejected.connect(setModuleOfTraction.reject)
        QtCore.QMetaObject.connectSlotsByName(setModuleOfTraction)

    def retranslateUi(self, setModuleOfTraction):
        _translate = QtCore.QCoreApplication.translate
        setModuleOfTraction.setWindowTitle(_translate("setModuleOfTraction", "Traction module window"))
        self.label.setText(_translate("setModuleOfTraction", "Module of traction (MPa): "))
