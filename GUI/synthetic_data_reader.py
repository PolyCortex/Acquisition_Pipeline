from time import time, sleep
from math import pi
from numpy import sin
import numpy as np
import threading


class CreateSyntheticData(threading.Thread):
    def __init__(self, callback, q_len=4000, read_freq=2000, N_CH=8):
        super().__init__()
        self.callback = callback
        self.q_len = q_len
        self.N_CH = N_CH

        self.i = 0
        self.read_period = 1/read_freq
        # signal
        amplitude1 = 10
        amplitude2 = 1
        omega1 = 1
        omega2 = 30
        t = np.linspace(0, 2 * pi, q_len)

        self.s1 = amplitude1 * sin(omega1*t)
        self.s2 = amplitude2 * sin(omega2*t)

    def run(self):
        self.create_synthetic_data()

    def create_synthetic_data(self):
        while 1:
            if self.i == self.q_len:
                self.i = 0

            one_value = self.s1[self.i] + self.s2[self.i]
            all_ch_values = [one_value for _ in range(self.N_CH)]
            self.callback(all_ch_values)

            self.i += 1
            sleep(self.read_period)



