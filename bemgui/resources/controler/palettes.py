from PyQt5.QtGui import QPalette, QColor
from PyQt5 import QtCore

dark_palette = QPalette()
dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
dark_palette.setColor(QPalette.WindowText, QColor(255, 140, 0))
dark_palette.setColor(QPalette.Base, QColor(150, 150, 150))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, QColor(150, 150, 150))
dark_palette.setColor(QPalette.ToolTipText, QColor(255, 140, 0))
dark_palette.setColor(QPalette.Text, QColor(255, 140, 0))
dark_palette.setColor(QPalette.Button, QColor(53, 59, 72))
dark_palette.setColor(QPalette.ButtonText, QColor(255, 140, 0))
dark_palette.setColor(QPalette.BrightText, QColor(255, 140, 0))
dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, QColor(255, 140, 0))



light_palette = QPalette()
light_palette.setColor(QPalette.Window, QColor(200, 200, 200))
light_palette.setColor(QPalette.WindowText, QColor(30, 30, 30))
light_palette.setColor(QPalette.Base, QColor(245, 246, 250))
light_palette.setColor(QPalette.AlternateBase, QtCore.Qt.red)
light_palette.setColor(QPalette.ToolTipBase, QtCore.Qt.black)
light_palette.setColor(QPalette.ToolTipText, QtCore.Qt.black)
light_palette.setColor(QPalette.Text, QtCore.Qt.black)
light_palette.setColor(QPalette.Button, QColor(195, 190, 190))
light_palette.setColor(QPalette.ButtonText, QtCore.Qt.black)
light_palette.setColor(QPalette.BrightText, QtCore.Qt.red)
light_palette.setColor(QPalette.Link, QColor(42, 130, 218))
light_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
light_palette.setColor(QPalette.HighlightedText, QtCore.Qt.blue)
