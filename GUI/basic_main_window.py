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
        self.q = deque(np.random.random(100), maxlen=100)
        plot = pg.PlotWidget()
        layout.addWidget(plot)
        self.curve = plot.plot(self.q)

    def update(self):
        self.q.append(np.random.random())
        self.curve.setData(self.q)

def create_timer(update_func):
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update_func)
    timer.start(50)
    return timer


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWin()
    timer = create_timer(main_window.plot_widget.update)

    sys.exit(app.exec_())
