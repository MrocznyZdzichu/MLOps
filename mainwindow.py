# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import qdarkstyle

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QFrame
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from DataRepository import DataRepository
from dl_tab_manager import DL_Tab
from dr_tab_manager import DR_Tab
from de_tab_manager import DE_Tab

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        window = uic.loadUi('mainwindow.ui', self)
        window.show()
        self.__tabs_indices = {
            0 : "DataLoader"
            , 1 : "DataRepository"
            , 2 : "DataExplorer"
        }
        self.__tabs_sizes = {
            0 : (480, 320)
            , 1 : (1000, 800)
            , 2 : (1800, 900)
        }

        curr_tab = self.tabWidget.currentIndex()
        self.resize(*self.__tabs_sizes[curr_tab])
        self.center_window(curr_tab)

        self.__repo_deployment = 'DataRepository_dir'
        repo = DataRepository(interactive=0
                            ,deployment_dir=self.__repo_deployment
        )
        self.DL_manager = DL_Tab(self, repo)
        self.DR_manager = DR_Tab(self, repo)
        self.DR_manager.initialize_tab()
        self.DE_manager = DE_Tab(self, repo)
        self.DE_manager.initialize_tab()

    #UI mainwindow slots do make this shiet live
    def change_size(self, tab_no):
        sizes = self.__tabs_sizes[tab_no]
        self.resize(*sizes)

    def center_window(self, tab_no):
        x_pos = (1920 - self.__tabs_sizes[tab_no][0]) / 2
        y_pos = (1080 - self.__tabs_sizes[tab_no][1]) / 4
        self.move(x_pos, y_pos)

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

    def add_DT_to_repo(self):
        self.DL_manager.add2repo()
        self.DR_manager.populate_cbs()
        self.DR_manager.switch_buttons()

    def drop_repo(self):
        self.DR_manager.drop_repo()

    def DR_add_DT_to_repo(self):
        self.DR_manager.add_table()

    def drop_DT_from_repo(self):
        self.DR_manager.drop_from_repo()

    def DR_browse_DT(self):
        self.DR_manager.browse_DT()

    def DE_tab_list_variables(self, selected_DT):
        self.DE_manager.populate_variables_table(selected_DT)
        self.DE_manager.UA_manager.populate_UA_cb()

    def DE_set_cbs_for_tool(self, selected_DE_tool):
        self.DE_manager.set_cbs_for_tool(selected_DE_tool)
        if selected_DE_tool == 'UnivariateAnalysis':
            self.DE_manager.UA_manager.populate_UA_cb()
        elif selected_DE_tool == 'BivariateAnalysis':
            self.DE_manager.BA_manager.populate_BA_cbs()

    def DE_set_UA_sw(self, variable):
        self.DE_manager.UA_manager.set_UA_sw(variable)

    def DE_exploration(self):
        self.DE_manager.exploration()

    def DE_replot_(self, plot_type):
        if plot_type == '':
            return
        self.DE_manager.UA_manager.replot_numeric(plot_type)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
