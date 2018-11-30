import threading
from queue import Queue

class Cleaner(threading.Thread):
    def __init__(self):
        super().__init__()

        self.queue8ChannelsList = Queue(maxsize=10)
        self.listQChannels = [Queue() for i in range(8)]

    def run(self):
        pass


