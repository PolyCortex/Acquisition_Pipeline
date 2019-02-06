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
        self.table_widget = TabWidget()
        self.setCentralWidget(self.table_widget)
        self.show()


class ScrollPlot(QWidget):
    def __init__(self):
        super().__init__()
        # Create the tab itself
        self.create_tab()

    def create_tab(self):
        l = QGridLayout(self)
        q = deque(np.random.random(1000), maxlen=1000)
        # p = pg.plot(q)
        p_w = pg.PlotWidget()
        self.curve = p_w.plot(q)
        p = self.curve.setData(q)
        l.addWidget(p)
        # self.l.addWidget(self.plot)
        self.setLayout(l)


class TabWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tabs.addTab(ScrollPlot(), 'Scroll plot')
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWin()
    main_window.show()
    sys.exit(app.exec_())

