import threading

from FileReader.FileReader import FileReader
import queue
import numpy
import time
import scipy.signal as filter

class Filter(threading.Thread):

    _TransmisionFrequency = 250
    _NbChannel = 8
    _LowPassFrequency = 50
    _HighPassFrequency = 10

    def __init__(self, outputQueue):
        super().__init__()
        self._input = queue.Queue()
        self._output = outputQueue  # de type queue.Queue
        self._rawData = numpy.zeros((self._TransmisionFrequency, self._NbChannel))

    def run(self):
        fileReader = FileReader(self.AddNewData, fileName="testBCI.csv", transmissionFrequency=250, startCSVcolumn=0, endCSVcolumn = 8)
        fileReader.start()

        ctr = 0;
        now = time.time()

        while True:
            newData = self._input.get()

            self.FilterNewData(newData)
            ctr += 1

            if ctr == 250:
                after = time.time()
                print(after - now)
                now = time.time()
                ctr = 0

        # fileReader.join()

    def AddNewData(self, newData):
        self._input.put(newData)

    def FilterNewData(self, newData):
        # TODO: checker ce que open bci envoi pour le comprendre
        self._rawData = self._rawData[:-1]
        newData = numpy.asarray(newData)
        self._rawData = numpy.vstack((newData, self._rawData))
        _filteredData = self.ApplyFilter()
        self._output.put(_filteredData)

    def ApplyFilter(self):
        highpass = self.WnTransform(self._HighPassFrequency)
        lowpass = self.WnTransform(self._LowPassFrequency)
        [b, a] = filter.butter(2, [highpass, lowpass], 'bandpass') # Pourrait sauvegarder ces donnees la dans l'objet
        filteredReading = []

        for i in range(0, self._NbChannel):
            filteredChannel = filter.filtfilt(b, a, self._rawData[:, i])
            filteredReading.append(filteredChannel[0])

        return filteredReading

    def WnTransform(self, frequency):
        return frequency / (0.5 * self._TransmisionFrequency)

    def stop(self):

        return


a = queue.Queue()
monFiltre = Filter(a)

monFiltre.start()
monFiltre.join()
