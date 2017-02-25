#reimplementing event handler - by pressing the esc button you terminate the application

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('reimplementing event handler')
        self.show()

    #rebinding esc button
    def keyPressEvent(self, event): #event is just a variable name
        if event.key() == Qt.Key_Escape:
            self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
