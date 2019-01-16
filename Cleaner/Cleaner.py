import threading
import queue
import time

class Cleaner(threading.Thread):
    def __init__(self, nbChannel=8):
        super().__init__()
        self.nbChannel = nbChannel
        self.queue8ChannelsList = queue.Queue(maxsize=10)
        self.listQChannels = [queue.Queue(maxsize= 1000) for i in range(self.nbChannel)]

    def run(self):
        while True:
            try:
                self.distributeChannel()
            except queue.Empty:
                pass




    def fetchData(self, data):
        self.queue8ChannelsList.put(data)

    def distributeChannel(self):
        for index, data in enumerate(self.queue8ChannelsList.get(block=False)):
            self.listQChannels[index].put(data)



a = Cleaner()

a.start()
