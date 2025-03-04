# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BemGui_Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindowUi(object):
    def setupUi(self, MainWindowUi):
        images_path = './bemgui/view/icons/'

        MainWindowUi.setObjectName("MainWindowUi")
        MainWindowUi.resize(1159, 678)
        icon = QtGui.QIcon.fromTheme("fusion")
        MainWindowUi.setWindowIcon(icon)
        MainWindowUi.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindowUi)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.createPoints = QtWidgets.QPushButton(self.groupBox)
        self.createPoints.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createPoints.setStyleSheet("")
        self.createPoints.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("{}AddPointIcon.png".format(images_path)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createPoints.setIcon(icon)
        self.createPoints.setCheckable(False)
        self.createPoints.setObjectName("createPoints")
        self.verticalLayout.addWidget(self.createPoints)
        self.createLines = QtWidgets.QPushButton(self.groupBox)
        self.createLines.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createLines.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("{}AddLineIcon.png".format(images_path)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createLines.setIcon(icon1)
        self.createLines.setIconSize(QtCore.QSize(50, 20))
        self.createLines.setObjectName("createLines")
        self.verticalLayout.addWidget(self.createLines)
        self.createArcs = QtWidgets.QPushButton(self.groupBox)
        self.createArcs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createArcs.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("{}AddCurvedElementsIcon.png".format(images_path)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createArcs.setIcon(icon2)
        self.createArcs.setIconSize(QtCore.QSize(40, 20))
        self.createArcs.setObjectName("createArcs")
        self.verticalLayout.addWidget(self.createArcs)
        self.defineZones = QtWidgets.QPushButton(self.groupBox)
        self.defineZones.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.defineZones.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("{}DefineZonesIcon.png".format(images_path)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.defineZones.setIcon(icon3)
        self.defineZones.setIconSize(QtCore.QSize(50, 20))
        self.defineZones.setObjectName("defineZones")
        self.verticalLayout.addWidget(self.defineZones)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.drawingArea = QtWidgets.QGraphicsView(self.centralWidget)
        self.drawingArea.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.drawingArea.setMouseTracking(True)
        self.drawingArea.setObjectName("drawingArea")
        self.gridLayout.addWidget(self.drawingArea, 0, 1, 3, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_3.setMaximumSize(QtCore.QSize(210, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.elastostaticStandard = QtWidgets.QRadioButton(self.groupBox_3)
        self.elastostaticStandard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.elastostaticStandard.setStyleSheet("")
        self.elastostaticStandard.setChecked(True)
        self.elastostaticStandard.setObjectName("elastostaticStandard")
        self.verticalLayout_3.addWidget(self.elastostaticStandard)
        self.elastostaticNoGrowth = QtWidgets.QRadioButton(self.groupBox_3)
        self.elastostaticNoGrowth.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.elastostaticNoGrowth.setObjectName("elastostaticNoGrowth")
        self.verticalLayout_3.addWidget(self.elastostaticNoGrowth)
        self.elatosticGrowth = QtWidgets.QRadioButton(self.groupBox_3)
        self.elatosticGrowth.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.elatosticGrowth.setObjectName("elatosticGrowth")
        self.verticalLayout_3.addWidget(self.elatosticGrowth)
        self.runElastosticAnalysis = QtWidgets.QPushButton(self.groupBox_3)
        self.runElastosticAnalysis.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.runElastosticAnalysis.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(220, 220, 220, 220), stop:1 rgba(170, 170, 170, 255));")
        self.runElastosticAnalysis.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("{}RunIcon.png".format(images_path)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runElastosticAnalysis.setIcon(icon4)
        self.runElastosticAnalysis.setObjectName("runElastosticAnalysis")
        self.verticalLayout_3.addWidget(self.runElastosticAnalysis)
        self.gridLayout.addWidget(self.groupBox_3, 0, 3, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        # self.BEM_MESH = QtWidgets.QRadioButton(self.groupBox_5)
        # self.BEM_MESH.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.BEM_MESH.setText("BEM")
        # self.BEM_MESH.setObjectName("BEM_MESH")
        # self.BEM_MESH.setMaximumSize(QtCore.QSize(50, 16777215))
        # self.BEM_MESH.setChecked(True)
        # self.verticalLayout_5.addWidget(self.BEM_MESH)
        # self.FEM_MESH = QtWidgets.QRadioButton(self.groupBox_5)
        # self.FEM_MESH.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.FEM_MESH.setText("FEM")
        # self.FEM_MESH.setObjectName("FEM_MESH")
        # self.FEM_MESH.setMaximumSize(QtCore.QSize(50, 16777215))
        # self.verticalLayout_5.addWidget(self.FEM_MESH)
        # self.MESHLESS = QtWidgets.QRadioButton(self.groupBox_5)
        # self.MESHLESS.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.MESHLESS.setText("MESHLESS")
        # self.MESHLESS.setObjectName("MESHLESS")
        # self.MESHLESS.setMaximumSize(QtCore.QSize(90, 16777215))
        # self.verticalLayout_5.addWidget(self.MESHLESS)
        self.Run_MESH = QtWidgets.QPushButton(self.groupBox_5)
        self.Run_MESH.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Run_MESH.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(220, 220, 220, 220), stop:1 rgba(170, 170, 170, 255));")
        self.Run_MESH.setText("")
        self.Run_MESH.setIcon(icon4)
        self.Run_MESH.setObjectName("Run_MESH")
        self.verticalLayout_5.addWidget(self.Run_MESH)
        self.gridLayout.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_6.setMaximumSize(QtCore.QSize(210, 16777215))
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.MESH_Deformed = QtWidgets.QPushButton(self.groupBox_6)
        self.MESH_Deformed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MESH_Deformed.setText("MESH DEFORMED")
        self.MESH_Deformed.setObjectName("MESH_Deformed")
        self.verticalLayout_6.addWidget(self.MESH_Deformed)
        self.MESH_Stresses = QtWidgets.QPushButton(self.groupBox_6)
        self.MESH_Stresses.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MESH_Stresses.setText("MESH STRESSES")
        self.MESH_Stresses.setObjectName("MESH_Stresses")
        self.verticalLayout_6.addWidget(self.MESH_Stresses)
        self.stressIntensityFactors = QtWidgets.QPushButton(self.groupBox_6)
        self.stressIntensityFactors.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stressIntensityFactors.setText("MESH INTENSITY FACTORS")
        self.stressIntensityFactors.setObjectName("stressIntensityFactors")
        self.verticalLayout_6.addWidget(self.stressIntensityFactors)
        self.crackGrowthPath = QtWidgets.QPushButton(self.groupBox_6)
        self.crackGrowthPath.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.crackGrowthPath.setText("CRACK GROWTH PATH")
        self.crackGrowthPath.setObjectName("crackGrowthPath")
        self.verticalLayout_6.addWidget(self.crackGrowthPath)
        self.fatigueLife = QtWidgets.QPushButton(self.groupBox_6)
        self.fatigueLife.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fatigueLife.setText("FATIGUE LIFE")
        self.fatigueLife.setObjectName("fatigueLife")
        self.verticalLayout_6.addWidget(self.fatigueLife)
        self.cracksSpreading = QtWidgets.QPushButton(self.groupBox_6)
        self.cracksSpreading.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cracksSpreading.setText("CRACKS SPREADING")
        self.cracksSpreading.setObjectName("cracksSpreading")
        self.verticalLayout_6.addWidget(self.cracksSpreading)
        self.runGraphicalResults = QtWidgets.QPushButton(self.groupBox_6)
        self.runGraphicalResults.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.runGraphicalResults.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(220, 220, 220, 220), stop:1 rgba(170, 170, 170, 255));")
        self.runGraphicalResults.setText("")
        self.runGraphicalResults.setIcon(icon4)
        self.runGraphicalResults.setObjectName("runGraphicalResults")
        self.verticalLayout_6.addWidget(self.runGraphicalResults)
        self.gridLayout.addWidget(self.groupBox_6, 1, 3, 3, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addDisplacement = QtWidgets.QPushButton(self.groupBox_2)
        self.addDisplacement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addDisplacement.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("{}DisplacementIcon.png".format(images_path)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addDisplacement.setIcon(icon5)
        self.addDisplacement.setIconSize(QtCore.QSize(100, 20))
        self.addDisplacement.setObjectName("addDisplacement")
        self.verticalLayout_2.addWidget(self.addDisplacement)
        self.addTraction = QtWidgets.QPushButton(self.groupBox_2)
        self.addTraction.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addTraction.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("{}TractionIcon.png".format(images_path)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addTraction.setIcon(icon6)
        self.addTraction.setIconSize(QtCore.QSize(100, 20))
        self.addTraction.setObjectName("addTraction")
        self.verticalLayout_2.addWidget(self.addTraction)
        # self.addConstrain = QtWidgets.QPushButton(self.groupBox_2)
        # self.addConstrain.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.addConstrain.setText("")
        # icon7 = QtGui.QIcon()
        # icon7.addPixmap(QtGui.QPixmap("{}unknownConstrainIcon.png".format(images_path)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.addConstrain.setIcon(icon7)
        # self.addConstrain.setIconSize(QtCore.QSize(100, 20))
        # self.addConstrain.setObjectName("addConstrain")
        # self.verticalLayout_2.addWidget(self.addConstrain)
        # self.Run_BoundaryConditions = QtWidgets.QPushButton(self.groupBox_2)
        # self.Run_BoundaryConditions.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.Run_BoundaryConditions.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(220, 220, 220, 220), stop:1 rgba(170, 170, 170, 255));")
        # self.Run_BoundaryConditions.setText("")
        # self.Run_BoundaryConditions.setIcon(icon4)
        # self.Run_BoundaryConditions.setObjectName("Run_BoundaryConditions")
        # self.verticalLayout_2.addWidget(self.Run_BoundaryConditions)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 2, 1)
        # self.groupBox_4 = QtWidgets.QGroupBox(self.centralWidget)
        # self.groupBox_4.setMaximumSize(QtCore.QSize(210, 16777215))
        # self.groupBox_4.setObjectName("groupBox_4")
        # self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        # self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        # self.verticalLayout_4.setSpacing(6)
        # self.verticalLayout_4.setObjectName("verticalLayout_4")
        # self.informationTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_4)
        # self.informationTextEdit.setUndoRedoEnabled(False)
        # self.informationTextEdit.setReadOnly(True)
        # self.informationTextEdit.setObjectName("informationTextEdit")
        # self.verticalLayout_4.addWidget(self.informationTextEdit)
        # self.gridLayout.addWidget(self.groupBox_4, 2, 3, 2, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 140))
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.inputDataButton = QtWidgets.QPushButton(self.groupBox_7)
        self.inputDataButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inputDataButton.setObjectName("inputDataButton")
        self.horizontalLayout_2.addWidget(self.inputDataButton)
        self.gridLayout.addWidget(self.groupBox_7, 3, 1, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_8.setMaximumSize(QtCore.QSize(16777215, 140))
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scaleButton = QtWidgets.QPushButton(self.groupBox_8)
        self.scaleButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scaleButton.setObjectName("scaleButton")
        self.horizontalLayout.addWidget(self.scaleButton)
        self.gridCheckBox = QtWidgets.QCheckBox(self.groupBox_8)
        self.gridCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridCheckBox.setObjectName("gridCheckBox")
        self.horizontalLayout.addWidget(self.gridCheckBox)
        self.incidenceCheckBox = QtWidgets.QCheckBox(self.groupBox_8)
        self.incidenceCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.incidenceCheckBox.setObjectName("incidenceCheckBox")
        self.horizontalLayout.addWidget(self.incidenceCheckBox)
        self.xLineEdit = QtWidgets.QLineEdit(self.groupBox_8)
        self.xLineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.xLineEdit.setStyleSheet("QLineEdit, QLineEdit:hover {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 1px solid #dddddd;\n"
"    color: #dddddd;\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QLineEdit:editable{\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #b2dfdb;\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #eeeeee;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"    color: #111111;\n"
"}\n"
"QLineEdit:pressed {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"}")
        self.xLineEdit.setInputMask("")
        self.xLineEdit.setPlaceholderText("")
        self.xLineEdit.setObjectName("xLineEdit")
        self.horizontalLayout.addWidget(self.xLineEdit)
        self.label = QtWidgets.QLabel(self.groupBox_8)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.yLineEdit = QtWidgets.QLineEdit(self.groupBox_8)
        self.yLineEdit.setStyleSheet("QLineEdit, QLineEdit:hover {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 1px solid #dddddd;\n"
"    color: #dddddd;\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QLineEdit:editable{\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #b2dfdb;\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #eeeeee;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"    color: #111111;\n"
"}\n"
"QLineEdit:pressed {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"}")
        self.yLineEdit.setInputMask("")
        self.yLineEdit.setObjectName("yLineEdit")
        self.horizontalLayout.addWidget(self.yLineEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox_8)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.aboutButton = QtWidgets.QPushButton(self.groupBox_8)
        self.aboutButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aboutButton.setObjectName("aboutButton")
        self.horizontalLayout.addWidget(self.aboutButton)
        self.gridLayout.addWidget(self.groupBox_8, 3, 2, 1, 1)
        MainWindowUi.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindowUi)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1159, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuBEMLAB = QtWidgets.QMenu(self.menuBar)
        self.menuBEMLAB.setObjectName("menuBEMLAB")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuTheme = QtWidgets.QMenu(self.menuView)
        self.menuTheme.setObjectName("menuTheme")
        MainWindowUi.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindowUi)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindowUi.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        MainWindowUi.insertToolBarBreak(self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindowUi)
        self.statusBar.setObjectName("statusBar")
        MainWindowUi.setStatusBar(self.statusBar)
        self.actionUndo = QtWidgets.QAction(MainWindowUi)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindowUi)
        self.actionRedo.setObjectName("actionRedo")
        self.actionNew = QtWidgets.QAction(MainWindowUi)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindowUi)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindowUi)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindowUi)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionLight = QtWidgets.QAction(MainWindowUi)
        self.actionLight.setObjectName("actionLight")
        self.actionDark = QtWidgets.QAction(MainWindowUi)
        self.actionDark.setObjectName("actionDark")
        self.menuBEMLAB.addAction(self.actionNew)
        self.menuBEMLAB.addAction(self.actionOpen)
        self.menuBEMLAB.addAction(self.actionSave)
        self.menuBEMLAB.addAction(self.actionSave_as)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuTheme.addAction(self.actionLight)
        self.menuTheme.addAction(self.actionDark)
        self.menuView.addAction(self.menuTheme.menuAction())
        self.menuBar.addAction(self.menuBEMLAB.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindowUi)
        QtCore.QMetaObject.connectSlotsByName(MainWindowUi)

    def retranslateUi(self, MainWindowUi):
        _translate = QtCore.QCoreApplication.translate
        MainWindowUi.setWindowTitle(_translate("MainWindowUi", "BEMGUI"))
        self.groupBox.setTitle(_translate("MainWindowUi", "Geometry"))
        self.createPoints.setToolTip(_translate("MainWindowUi", "Add points"))
        self.createLines.setToolTip(_translate("MainWindowUi", "Add lines"))
        self.createArcs.setToolTip(_translate("MainWindowUi", "Add curved elements"))
        self.defineZones.setToolTip(_translate("MainWindowUi", "Change zones characteristics"))
        self.groupBox_3.setTitle(_translate("MainWindowUi", "ELASTOTATIC ANALYSIS"))
        self.elastostaticStandard.setText(_translate("MainWindowUi", "STANDARD BEM"))
        self.elastostaticNoGrowth.setText(_translate("MainWindowUi", "WITH NO CRACK GROWTH"))
        self.elatosticGrowth.setText(_translate("MainWindowUi", "WITH CRACK GROWTH"))
        self.runElastosticAnalysis.setToolTip(_translate("MainWindowUi", "Run Elastostatic analysis"))
        self.groupBox_5.setTitle(_translate("MainWindowUi", "MESH"))
        self.Run_MESH.setToolTip(_translate("MainWindowUi", "Run MESH"))
        self.groupBox_6.setTitle(_translate("MainWindowUi", "GRAPHICAL RESULTS"))
        self.runGraphicalResults.setToolTip(_translate("MainWindowUi", "Run graphical results"))
        self.groupBox_2.setTitle(_translate("MainWindowUi", "BOUNDARY CONDITIONS"))
        self.addDisplacement.setToolTip(_translate("MainWindowUi", "Add displacement"))
        self.addTraction.setToolTip(_translate("MainWindowUi", "Add traction"))
        # self.addConstrain.setToolTip(_translate("MainWindowUi", "Add unknown constrain"))
        self.groupBox_7.setTitle(_translate("MainWindowUi", "INPUT DATA"))
        self.inputDataButton.setText(_translate("MainWindowUi", "Data"))
        self.groupBox_8.setTitle(_translate("MainWindowUi", "SCALE DATA"))
        self.scaleButton.setText(_translate("MainWindowUi", "Scale"))
        self.gridCheckBox.setText(_translate("MainWindowUi", "Grid"))
        self.incidenceCheckBox.setText(_translate("MainWindowUi", "Incidence"))
        self.xLineEdit.setText(_translate("MainWindowUi", "1.0"))
        self.label.setText(_translate("MainWindowUi", "m"))
        self.yLineEdit.setText(_translate("MainWindowUi", "1.0"))
        self.label_2.setText(_translate("MainWindowUi", "m"))
        self.aboutButton.setText(_translate("MainWindowUi", "About!"))
        self.menuBEMLAB.setTitle(_translate("MainWindowUi", "File"))
        self.menuEdit.setTitle(_translate("MainWindowUi", "Edit"))
        self.menuView.setTitle(_translate("MainWindowUi", "View"))
        self.menuTheme.setTitle(_translate("MainWindowUi", "Theme"))
        self.actionUndo.setText(_translate("MainWindowUi", "Undo"))
        self.actionRedo.setText(_translate("MainWindowUi", "Redo"))
        self.actionNew.setText(_translate("MainWindowUi", "New"))
        self.actionOpen.setText(_translate("MainWindowUi", "Open"))
        self.actionSave.setText(_translate("MainWindowUi", "Save"))
        self.actionSave_as.setText(_translate("MainWindowUi", "Save As"))
        self.actionLight.setText(_translate("MainWindowUi", "Light"))
        self.actionDark.setText(_translate("MainWindowUi", "Dark"))
