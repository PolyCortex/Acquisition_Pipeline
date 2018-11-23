import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import numpy as np
from numpy import pi, sin
from collections import deque
from scipy.signal import butter, lfilter, freqz, filtfilt
import matplotlib.pyplot as plt
from time import time


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


win = pg.GraphicsWindow()
p = win.addPlot()
p2 = win.addPlot(1, 0)

N_DATA = 1250
t = np.linspace(0, 2 * pi, N_DATA)
## signal shape
i = 0
m = 1
s1 = m * sin(3 * t)
s2 = m * sin(10 * t)
s3 = m * sin(60 * t)
data = deque(np.zeros(N_DATA), maxlen=N_DATA)
viz_data = deque(np.zeros(N_DATA), maxlen=N_DATA)
solo_sin = deque(np.zeros(N_DATA), maxlen=N_DATA)

c1 = p.plot(data)
c1.setPen('r')
c2 = p.plot(data)
c2.setPen('w')
c3 = p.plot(data)
c3.setPen('g')

# Filter requirements.
order = 5
fs = 250.0       # sample rate, Hz
cutoff = 5  # desired cutoff frequency of the filter, Hz

last_t = time()
last_n_data = 0
def update():
    global data, curve, i, order, fs, cutoff, viz_data, last_t, last_n_data
    i += 1
    last_n_data += 1
    if i == N_DATA:
        i = 0
    # if time() - last_t > 1:
    #     print('time greater')
    #     print(time()-last_t)
    #     print(last_n_data)
    #     freq =  last_n_data / (time()-last_t)
    #     print(f'frequency: ', freq)
    #     last_t = time()
    #     last_n_data = 0

    data.append(s1[i] + s2[i] + s3[i])
    solo_sin.append(s2[i])

    # TEST filter
    if i % 1 == 0:
        # print('Filtering ...')
        y = butter_bandpass_filter(data, 1, 6, fs, order)
        viz_data.append(y[-1])
        c1.setData(solo_sin)
        c2.setData(data)
        c3.setData(viz_data)

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(1/fs * 1000)


if __name__ == '__main__':

    QtGui.QApplication.instance().exec_()

