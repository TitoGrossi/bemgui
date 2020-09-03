from PyQt5 import QtWidgets
from bemgui.resources.controler.MainWindow import MainWindowApp
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyle("Fusion")

    ui = MainWindowApp()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
