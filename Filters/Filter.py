
import threading
from FileReader.FileReader import FileReader
import queue
import numpy
import scipy.signal as filter

class Filter(threading.Thread):

    _TransmisionFrequency = 250
    _NbChannel = 8
    _LowPassFrequency = 50
    _HighPassFrequency = 10

    def __init__(self, outputQueue):
        super().__init__()
        self._output = outputQueue  # de type queue.Queue
        self._rawData = numpy.zeros((self._TransmisionFrequency, self._NbChannel))

    def run(self):
        fileReader = FileReader(self.AddNewData, fileName ="input_data.csv", transmissionFrequency=250, startCSVcolumn=0, endCSVcolumn = 8)
        fileReader.start()
        fileReader.join()

    def AddNewData(self, newData):
        self._rawData = self._rawData[:-1]
        newData = numpy.asarray(newData)
        self._rawData = numpy.vstack((newData, self._rawData))
        _filteredData = self.ApplyFilter()
        print("[ " + str(_filteredData) +" ]")
        self._output.put(_filteredData)

    def ApplyFilter(self):
        highpass = self.WnTransform(self._HighPassFrequency)
        lowpass = self.WnTransform(self._LowPassFrequency)
        [b, a] = filter.butter(2, [highpass, lowpass], 'bandpass')
        _filteredData = filter.filtfilt(b, a, self._rawData[:,0])
        return _filteredData[0]

    def WnTransform(self, frequency):
        return frequency / ( 0.5 * self._TransmisionFrequency)

    def stop(self):

        return


a = queue.Queue()
monFiltre = Filter(a)

monFiltre.start()
monFiltre.join()
