# -*- coding: utf-8 -*-

import csv
import threading
import asyncio
import time

class FileReader(threading.Thread):
    """
    Class used to read a CSV format file and transmit data at a certain transmission frequency using callbacks.
    
    Purpose is to simulate real-time transmission, test filters and more.
    """

    
    def __init__(self, fetchData, fileName, startCSVcolumn, endCSVcolumn, transmissionFrequency=100, binary=False):
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
                extractedRow = list(map(float, extractedRow))
                self.dataQueue.append(extractedRow)

        print('Ready for transmission. Proceeding.')

        # Wait time (s)
        sleepTime = 1/self.transmissionFrequency

        for i in range(0, len(self.dataQueue)):
            #asyncio.run(self.fetchData(self.dataQueue[i]))
            self.fetchData(self.dataQueue[i])
            time.sleep(sleepTime)

        print('Process complete. Ending simulation.')
        return None
