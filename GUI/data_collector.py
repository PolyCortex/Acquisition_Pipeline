class DataCollector:
    def __init__(self, q):
        self.q = q

    def fetch_data(self, signal):
        self.q.append(signal)
