import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        #three labels
        title = QLabel('Title')
        band = QLabel('Band')
        review = QLabel('Review')

        #three widgets
        titleEdit = QLineEdit()
        bandEdit = QLineEdit()
        reviewEdit = QTextEdit()

        #setting layout
        grid = QGridLayout()
        grid.setSpacing(10) #not sure what spacing does

        #placing widgets
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(band, 2, 0)
        grid.addWidget(bandEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1) #specifying, that the 3rd widget will span 5 rows and 1 column

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
