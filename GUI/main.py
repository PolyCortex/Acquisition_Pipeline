# General packages
from PyQt5.QtWidgets import *
import sys
from Filters import Filter
# Our packages
from GUI.basic_main_window import MainWindow
from GUI.timer import create_timer
from GUI.synthetic_data_reader import CreateSyntheticData
from GUI.data_collector import DataCollector


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    timer = create_timer(main_window.plot_widget.update)

    # data_collector = DataCollector(main_window.plot_widget.all_q)
    # create_synthetic_data = CreateSyntheticData(data_collector.fetch_data)
    # create_synthetic_data.start()

    all_q = main_window.plot_widget.all_q

    filter = Filter.Filter(all_q)
    filter.start()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

