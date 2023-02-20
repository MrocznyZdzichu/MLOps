# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import qdarkstyle

import DataLoader as DL
import DataTable as DT


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

        self.loader = DL.DataLoader()

    #UI mainwindow slots do make this shiet live
    def change_size(self, tab_no):
        sizes = self.__tabs_sizes[tab_no]
        self.resize(*sizes)

    def load_data(self):
        self.__dl_log_msg('Initiate data loading: ...')
        try:
            self.__curr_DT = self.loader.load_data()
        except:
            self.__dl_log_msg('An error occured during loading the data')
        else:
            self.__dl_log_msg('Data loaded successfully')
            self.__dl_post_loading_pb_switch()

    def load_pickle(self):
        self.__dl_log_msg('Initiate data loading: ...')
        try:
            self.__curr_DT = self.loader.load_saved_DT()
        except:
            self.__dl_mog_msg('An error occured during loading the pickle')
        else:
            self.__dl_log_msg('Data loaded successfully')
            self.__dl_post_loading_pb_switch()

    def clear_curr_DT(self):
        del self.__curr_DT
        self.__dl_log_msg('Current DataTable cleared')
        self.__dl_post_clearing_pb_switch()

    def save_DT(self):
        self.__dl_log_msg('Saving the DataTable')
        try:
            self.__curr_DT.save()
        except:
            self.__dl_log_msg('An error occured during saving the DataTable')
        else:
            self.__dl_log_msg('Saving successful')

    #submethods
    def __dl_log_msg(self, msg):
        self.dl_tb_log_console.append(msg)

    def __dl_post_loading_pb_switch(self):
        self.dl_pb_load_data.setDisabled(1)
        self.dl_pb_load_pickle.setDisabled(1)
        self.dl_pb_clear.setEnabled(1)
        self.dl_pb_save_pickle.setEnabled(1)
        self.dl_pb_summary.setEnabled(1)

    def __dl_post_clearing_pb_switch(self):
        self.dl_pb_load_data.setEnabled(1)
        self.dl_pb_load_pickle.setEnabled(1)
        self.dl_pb_clear.setDisabled(1)
        self.dl_pb_save_pickle.setDisabled(1)
        self.dl_pb_summary.setDisabled(1)

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
