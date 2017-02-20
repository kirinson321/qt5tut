#this program is both toolbar.py and core.py joined together
#remember that YOU create actions, such as exitAction

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon



class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit) #wow, that's pretty powerful function

        exitAction = QAction(QIcon('five.jpg'), "Exit", self) #creating a label
        exitAction.setShortcut('Ctrl+Q') #keyboard shortcut
        exitAction.setStatusTip('Exit the app') #info box appearing on mouse hover
        exitAction.triggered.connect(self.close) #connection?
        #what's the purpose of creating connection in line 22, if it's specified above that the app will close (label in line 19)

        self.statusBar() #shown in the lower part of the window

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File') #naming the menubar's position
        fileMenu.addAction(exitAction) #binding action

        toolbar = self.addToolBar('Exit') #same as menubar, but with icons - most commonly used positions from menubar are usually held here
        toolbar.addAction(exitAction) #binding action created by us

        #givin the window looks
        self.setGeometry(300, 300, 350, 250) #displacement on screen and width with height
        self.setWindowTitle('fusion') #self explanatory
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
