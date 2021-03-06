import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon



class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        exitAction = QAction(QIcon('five.jpg'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        #exitAction.setStatusTip('Exit application'); works only for menubars
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar tutorial')
        self.show()

'''
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
