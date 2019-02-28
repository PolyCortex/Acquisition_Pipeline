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
        self.layout = QGridLayout(self)
        self.all_curves, self.all_q = self.create_all_curves_and_all_q()

    def create_all_curves_and_all_q(self):
        all_curves = []
        all_q = []
        for _ in range(8):
            q = deque(np.zeros(1250), maxlen=1250)
            all_q.append(q)
            curve = self.create_curve(q)
            all_curves.append(curve)
        return all_curves, all_q

    def create_curve(self, q):
        plot = pg.PlotWidget()
        self.layout.addWidget(plot)
        curve = plot.plot(q)
        return curve

    def update(self):
        for q, curve in zip(self.all_q, self.all_curves):
            curve.setData(q)




