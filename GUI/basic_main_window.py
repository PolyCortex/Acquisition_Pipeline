from PyQt5.QtWidgets import *
import pyqtgraph as pg
from collections import deque
import numpy as np


class MainWindow(QMainWindow):
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
        self.q = deque(np.zeros(1250), maxlen=1250)
        plot = pg.PlotWidget()
        layout.addWidget(plot)
        self.curve = plot.plot(self.q)

    def update(self):
        self.curve.setData(self.q)




