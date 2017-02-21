#absolute positioning layout
#I suppose electron based apps are written more simply
#that kind of layout is ineffective 
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        label1 = QLabel('Test', self)
        label1.move(15,10)

        label2 = QLabel('PyQt5', self)
        label2.move(35, 40)

        label3 = QLabel('amatorka', self)
        label3.move(55, 70)

        self.setGeometry(300, 200, 250, 150)
        self.setWindowTitle('absolute layout')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
