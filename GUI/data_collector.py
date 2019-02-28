class DataCollector:
    def __init__(self, all_q):
        self.all_q = all_q

    def fetch_data(self, all_ch_signal):
        for q, ch_signal in zip(self.all_q, all_ch_signal):
            q.append(ch_signal)
