import sys
from PyQt5.QtWidgets import *


class MainWin(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.show()


class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        b = QPushButton('button')
        self.layout.addWidget(b)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWin()
    sys.exit(app.exec_())