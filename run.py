from PyQt5 import QtWidgets
from bemgui.controller.mainwindow import MainWindow
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyle("Fusion")

    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
