from PyQt5 import QtWidgets, QtGui, QtCore

class xPosition(QtWidgets.QLineEdit):
    def __init__(self, mainwindow):
        QtWidgets.QLineEdit.__init__(self)
        self.mainwindow = mainwindow
        self.setText("0.00")
        self.setParent(self.mainwindow.drawingArea)
        self.setValidator(QtGui.QDoubleValidator())
        self.returnPressed.connect(self.changeFocusToY)

    def changeFocusToY(self):
        self.mainwindow.yPos.setFocus()
        self.mainwindow.yPos.selectAll()


class yPosition(QtWidgets.QLineEdit):
    def __init__(self, mainwindow):
        QtWidgets.QLineEdit.__init__(self)
        self.mainwindow = mainwindow
        self.setText("0.00")
        self.setParent(self.mainwindow.drawingArea)
        self.setValidator(QtGui.QDoubleValidator())
        self.returnPressed.connect(self.addPointToScene)

        validator = QtGui.QDoubleValidator()
        validator.setDecimals(2)
        validator.setLocale(QtCore.QLocale())
        self.setValidator(validator)

    def addPointToScene(self):
        x = float(self.mainwindow.xPos.text()) * 1000
        y = float(self.text()) * 1000
        self.mainwindow.scene.addPoint(QtCore.QPointF(x, -y))
        self.mainwindow.xPos.setFocus()
        self.mainwindow.xPos.selectAll()


class status_bar(QtWidgets.QLabel):
    def __init__(self, mainwindow):
        QtWidgets.QTextEdit.__init__(self)
        self.mainwindow = mainwindow
        self.setParent(self.mainwindow.drawingArea)
        self.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.unshow)
        #self.setStyleSheet("background-color: yellow;")

    def show_message(self, msg):
        self.setText(msg)
        left = self.parent().mapToParent(self.parent().rect().bottomLeft()).x()
        right = self.parent().mapToParent(self.parent().rect().bottomRight()).x()
        top = self.parent().mapToParent(self.parent().rect().bottomRight()).y() - 45
        width = right - left
        self.setGeometry(left, top, width - 200, 30)
        self.setVisible(True)
        self.timer.start()

    def unshow(self):
        self.setVisible(False)

    def update_pos(self):
        left = self.parent().mapToParent(self.parent().rect().bottomRight()).x() - 300
        top = self.parent().mapToParent(self.parent().rect().bottomRight()).y() - 45
        self.setGeometry(left, top, 100, 30)
