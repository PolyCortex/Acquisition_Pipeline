import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import numpy as np
from collections import deque
from random import random

win = pg.GraphicsWindow()

class BasicScroll:
    def __init__(self, win):
        win.nextRow()
        p = win.addPlot(colspan=2)
        self.d1 = deque(np.zeros(1000), maxlen=1000)
        self.c1 = p.plot(self.d1)

    def update(self):
        self.d1.append(random())
        self.c1.setData(self.d1)

basic_scroll = BasicScroll(win)

timer = pg.QtCore.QTimer()
timer.timeout.connect(basic_scroll.update)
timer.start(50)


if __name__ == '__main__':

    QtGui.QApplication.instance().exec_()

