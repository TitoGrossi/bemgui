# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalCrackDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FinalCrackDialog(object):
    def setupUi(self, FinalCrackDialog):
        FinalCrackDialog.setObjectName("FinalCrackDialog")
        FinalCrackDialog.resize(400, 415)
        self.gridLayout_2 = QtWidgets.QGridLayout(FinalCrackDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(FinalCrackDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 4, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(FinalCrackDialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(FinalCrackDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 2)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 3, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 2, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(FinalCrackDialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.gridLayout_2.addWidget(self.groupBox_3, 3, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(175, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(FinalCrackDialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 1, 2)

        self.retranslateUi(FinalCrackDialog)
        self.buttonBox.accepted.connect(FinalCrackDialog.accept)
        self.buttonBox.rejected.connect(FinalCrackDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FinalCrackDialog)

    def retranslateUi(self, FinalCrackDialog):
        _translate = QtCore.QCoreApplication.translate
        FinalCrackDialog.setWindowTitle(_translate("FinalCrackDialog", "Dialog"))
        self.groupBox.setTitle(_translate("FinalCrackDialog", "Growth Steps"))
        self.label.setText(_translate("FinalCrackDialog", "Increment Number:"))
        self.label_2.setText(_translate("FinalCrackDialog", "Increment Size (x crack-tipelement):"))
        self.groupBox_2.setTitle(_translate("FinalCrackDialog", "Paris Parameters"))
        self.label_6.setText(_translate("FinalCrackDialog", "da/dn = C.Keq^m"))
        self.label_3.setText(_translate("FinalCrackDialog", "C:"))
        self.label_4.setText(_translate("FinalCrackDialog", "m:"))
        self.label_5.setText(_translate("FinalCrackDialog", "Stress Ratio:"))
        self.groupBox_3.setTitle(_translate("FinalCrackDialog", "Gauss Point"))
        self.label_7.setText(_translate("FinalCrackDialog", "Increase Number:"))
        self.groupBox_4.setTitle(_translate("FinalCrackDialog", "Problem type"))
