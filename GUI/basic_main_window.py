from PyQt5.QtWidgets import *
import pyqtgraph as pg
from collections import deque
import numpy as np
import sys


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.plot_widget = PlotWidget()
        self.setCentralWidget(self.plot_widget)
        self.show()


class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout(self)
        q = deque(np.random.random(100), maxlen=100)
        plot = pg.PlotWidget()
        layout.addWidget(plot)
        plot.plot(q)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainWin()
    sys.exit(app.exec_())
