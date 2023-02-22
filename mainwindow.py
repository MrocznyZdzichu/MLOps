# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import qdarkstyle

from  dl_tab_manager import DL_Tab

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        window = uic.loadUi('mainwindow.ui', self)
        window.show()
        self.__tabs_indices = {
            0 : "DataLoader"
        }
        self.__tabs_sizes = {
            0 : (480, 320)
        }
        self.resize(*self.__tabs_sizes[0])

        self.DL_manager = DL_Tab(self)

    #UI mainwindow slots do make this shiet live
    def change_size(self, tab_no):
        sizes = self.__tabs_sizes[tab_no]
        self.resize(*sizes)

    def load_data(self):
        self.DL_manager.load_data()

    def load_pickle(self):
        self.DL_manager.load_pickle()

    def clear_curr_DT(self):
        self.DL_manager.clear_curr_DT()

    def save_DT(self):
        self.DL_manager.save_DT()

    def print_summary(self):
        self.DL_manager.print_summary()


if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
