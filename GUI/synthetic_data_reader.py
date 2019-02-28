from time import time, sleep
from math import pi
from numpy import sin
import numpy as np
import threading


class CreateSyntheticData(threading.Thread):
    def __init__(self, callback, q_len=1250, read_freq=250):
        super().__init__()
        self.callback = callback
        self.q_len = q_len

        self.i = 0
        self.read_period = 1/read_freq
        # signal
        amplitude = 1000
        omega = 10
        t = np.linspace(0, 2 * pi, q_len)
        self.s = amplitude * sin(omega*t)

    def run(self):
        self.create_synthetic_data()

    def create_synthetic_data(self):
        while 1:
            if self.i == self.q_len:
                self.i = 0

            one_value = self.s[self.i]
            self.callback(one_value)

            self.i += 1
            sleep(self.read_period)



