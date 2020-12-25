# TODO: put this on a more well placed file with the widgets used to inform the user
# (informUser.py)

from PyQt5 import QtWidgets

class disabableLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent):
        super(disabableLineEdit, self).__init__(parent)

    def updateTextIfParentIsDisabled(self, text):
        if not self.parent().isEnabled():
            self.setText(text)

class disabableCheckBox(QtWidgets.QCheckBox):
    def __init__(self, parent):
        super(disabableCheckBox, self).__init__(parent)

    def toggleIfParentIsDisabled(self, bool):
        if not self.parent().isEnabled():
            self.setChecked(bool)
