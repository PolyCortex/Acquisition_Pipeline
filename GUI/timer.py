import pyqtgraph as pg


def create_timer(update_func):
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update_func)
    timer.start(50)
    return timer

