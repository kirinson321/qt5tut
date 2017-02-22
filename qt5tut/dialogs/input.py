# simple input dialog box

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.button = QPushButton('Dialog', self)
        self.button.move(20, 20)
        self.button.clicked.connect(self.showDialog)
        #sending a signal to show the dialog window, specified below

        self.line = QLineEdit(self)
        self.setWindowTitle('Input dialog')
        self.show()


    def showDialog(self):
        #not sure how this "text, ok" works, lol
        text, ok = QInputDialog.getText(self, 'Input dialog', 'Enter your name:')
        if ok:
            self.line.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
