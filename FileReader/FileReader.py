# -*- coding: utf-8 -*-

import csv
import threading
from time import sleep, thread_time, time_ns

class FileReader(threading.Thread):
    """
    Class used to read a CSV format file and transmit data at a certain transmission frequency using callbacks.
    
    Purpose is to simulate real-time transmission, test filters and more.
    """

    
    def __init__(self, fetchData, fileName, transmissionFrequency, startCSVcolumn, endCSVcolumn, binary=False):
        #super(FileReader, self).__init__()
        threading.Thread.__init__(self)
        # Callback
        self.fetchData = fetchData

        # Filename for the CSV format file
        self.fileName = fileName

        # Data to transmit
        self.dataQueue = []

        # Transmission Frequency (Hz)
        self.transmissionFrequency = transmissionFrequency

        # Starting column for the data in CSV
        self.startCSVcolumn = startCSVcolumn

        # Ending column for the data in CSV
        self.endCSVcolumn = endCSVcolumn

        # Reading in binary
        self.binary = binary

    def run(self):
        """Reads data from file then calls the callback at a certain frequency."""     
        print('Reading file for simulation...', flush=True)

        openMode = 'rb' if self.binary else 'r' 
        with open(self.fileName, openMode) as csvFile:
            reader = csv.reader(csvFile, delimiter=',')
            for row in reader:
                extractedRow = row[self.startCSVcolumn:self.endCSVcolumn].copy()
                self.dataQueue.append(extractedRow)

        print('Ready for transmission. Proceeding.')

        #The nanoseconds to wait
        desiredTransmissionTime = 1000000000.0/self.transmissionFrequency

        print(len(self.dataQueue))
        for i in range(0, len(self.dataQueue)):
            transmissionStartTime = time_ns()

            self.fetchData(self.dataQueue[i])

            transmissionEndTime = time_ns()

            transmissionDuration = transmissionEndTime - transmissionStartTime

            while transmissionDuration < desiredTransmissionTime:
                sleepTime = ( desiredTransmissionTime - transmissionDuration )
                sleep(sleepTime/1000000000)
                transmissionDuration = time_ns() - transmissionStartTime

        print('Process complete. Ending simulation.')
        return None

def func(array):
    #Do Nothing
    x = 0

def main():
    fileReader = FileReader(func, "tests/input_data_1.csv", 250, 0, 8)
    #fileReader.start()
    fileReader.run()

if __name__ == '__main__':
    main()