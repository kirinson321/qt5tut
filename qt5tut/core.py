import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("Ready")
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Statusbar")
        self.show()




if __name__ =="__main__":

    app = QApplication(sys.argv)
    ex = Example()
    #w = QWidget() #creating new window
    #w.resize(350, 250)
    #w.move(300, 300)
    #w.setWindowTitle("First")
    #w.show()

    sys.exit(app.exec_())
