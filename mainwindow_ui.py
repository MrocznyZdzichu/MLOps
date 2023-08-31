# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1800, 900)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_15 = QGridLayout(self.centralwidget)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.DataLoader_tab = QWidget()
        self.DataLoader_tab.setObjectName(u"DataLoader_tab")
        self.gridLayout_2 = QGridLayout(self.DataLoader_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 35, 20, 25)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.dl_pb_clear = QPushButton(self.DataLoader_tab)
        self.dl_pb_clear.setObjectName(u"dl_pb_clear")
        self.dl_pb_clear.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dl_pb_clear.sizePolicy().hasHeightForWidth())
        self.dl_pb_clear.setSizePolicy(sizePolicy)
        self.dl_pb_clear.setMinimumSize(QSize(100, 0))
        self.dl_pb_clear.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_3.addWidget(self.dl_pb_clear, 0, Qt.AlignHCenter)

        self.dl_pb_save_pickle = QPushButton(self.DataLoader_tab)
        self.dl_pb_save_pickle.setObjectName(u"dl_pb_save_pickle")
        self.dl_pb_save_pickle.setEnabled(False)
        self.dl_pb_save_pickle.setMinimumSize(QSize(100, 0))
        self.dl_pb_save_pickle.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_3.addWidget(self.dl_pb_save_pickle, 0, Qt.AlignHCenter)

        self.dl_pb_summary = QPushButton(self.DataLoader_tab)
        self.dl_pb_summary.setObjectName(u"dl_pb_summary")
        self.dl_pb_summary.setEnabled(False)
        self.dl_pb_summary.setMinimumSize(QSize(100, 0))
        self.dl_pb_summary.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_3.addWidget(self.dl_pb_summary, 0, Qt.AlignHCenter)

        self.dl_pb_save_repo = QPushButton(self.DataLoader_tab)
        self.dl_pb_save_repo.setObjectName(u"dl_pb_save_repo")
        self.dl_pb_save_repo.setEnabled(False)
        self.dl_pb_save_repo.setMinimumSize(QSize(100, 0))
        self.dl_pb_save_repo.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_3.addWidget(self.dl_pb_save_repo, 0, Qt.AlignHCenter)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)

        self.dl_tb_log_console = QTextBrowser(self.DataLoader_tab)
        self.dl_tb_log_console.setObjectName(u"dl_tb_log_console")

        self.gridLayout.addWidget(self.dl_tb_log_console, 3, 0, 1, 2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setContentsMargins(50, -1, 50, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 0, 1, 3)

        self.dl_pb_load_pickle = QPushButton(self.DataLoader_tab)
        self.dl_pb_load_pickle.setObjectName(u"dl_pb_load_pickle")
        self.dl_pb_load_pickle.setMinimumSize(QSize(100, 0))
        self.dl_pb_load_pickle.setMaximumSize(QSize(100, 16777215))
        self.dl_pb_load_pickle.setLayoutDirection(Qt.LeftToRight)
        self.dl_pb_load_pickle.setAutoDefault(False)
        self.dl_pb_load_pickle.setFlat(False)

        self.gridLayout_3.addWidget(self.dl_pb_load_pickle, 3, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 4, 0, 1, 3)

        self.dl_pb_load_data = QPushButton(self.DataLoader_tab)
        self.dl_pb_load_data.setObjectName(u"dl_pb_load_data")
        self.dl_pb_load_data.setMinimumSize(QSize(100, 0))
        self.dl_pb_load_data.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.dl_pb_load_data, 3, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(3, 2)
        self.gridLayout_3.setRowStretch(4, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(2, 1)

        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 3)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 2)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.DataLoader_tab, "")
        self.DataRepository_tab = QWidget()
        self.DataRepository_tab.setObjectName(u"DataRepository_tab")
        self.gridLayout_6 = QGridLayout(self.DataRepository_tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(25, 15, 25, 15)
        self.dr_le_repo_loc = QLineEdit(self.DataRepository_tab)
        self.dr_le_repo_loc.setObjectName(u"dr_le_repo_loc")
        self.dr_le_repo_loc.setMinimumSize(QSize(300, 0))
        self.dr_le_repo_loc.setMaximumSize(QSize(300, 16777215))
        self.dr_le_repo_loc.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.dr_le_repo_loc, 0, Qt.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridWidget_3 = QWidget(self.DataRepository_tab)
        self.gridWidget_3.setObjectName(u"gridWidget_3")
        self.gridLayout_12 = QGridLayout(self.gridWidget_3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.dr_cb_DT_pick = QComboBox(self.gridWidget_3)
        self.dr_cb_DT_pick.setObjectName(u"dr_cb_DT_pick")

        self.gridLayout_12.addWidget(self.dr_cb_DT_pick, 2, 0, 1, 1)

        self.dr_pb_DT_remove = QPushButton(self.gridWidget_3)
        self.dr_pb_DT_remove.setObjectName(u"dr_pb_DT_remove")
        self.dr_pb_DT_remove.setEnabled(False)

        self.gridLayout_12.addWidget(self.dr_pb_DT_remove, 2, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_3, 0, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_4, 3, 0, 1, 2)

        self.dr_pb_DT_add = QPushButton(self.gridWidget_3)
        self.dr_pb_DT_add.setObjectName(u"dr_pb_DT_add")
        self.dr_pb_DT_add.setEnabled(True)

        self.gridLayout_12.addWidget(self.dr_pb_DT_add, 1, 0, 1, 2)

        self.gridLayout_12.setRowStretch(0, 1)
        self.gridLayout_12.setRowStretch(3, 1)
        self.gridLayout_12.setColumnStretch(0, 3)
        self.gridLayout_12.setColumnStretch(1, 2)

        self.horizontalLayout.addWidget(self.gridWidget_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(35, 5, 35, 20)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.DataRepository_tab)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.dr_tb_summary = QTextBrowser(self.DataRepository_tab)
        self.dr_tb_summary.setObjectName(u"dr_tb_summary")

        self.verticalLayout_5.addWidget(self.dr_tb_summary)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_4 = QLabel(self.DataRepository_tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_11.addWidget(self.label_4, 0, 0, 1, 1)

        self.dr_le_shapes = QLineEdit(self.DataRepository_tab)
        self.dr_le_shapes.setObjectName(u"dr_le_shapes")
        self.dr_le_shapes.setEnabled(True)
        self.dr_le_shapes.setReadOnly(True)

        self.gridLayout_11.addWidget(self.dr_le_shapes, 1, 0, 1, 1)

        self.label_3 = QLabel(self.DataRepository_tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_11.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_5 = QLabel(self.DataRepository_tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_11.addWidget(self.label_5, 2, 0, 1, 1)

        self.dr_le_register_dttm = QLineEdit(self.DataRepository_tab)
        self.dr_le_register_dttm.setObjectName(u"dr_le_register_dttm")
        self.dr_le_register_dttm.setEnabled(True)
        self.dr_le_register_dttm.setReadOnly(True)

        self.gridLayout_11.addWidget(self.dr_le_register_dttm, 3, 0, 1, 1)

        self.dr_tb_variables = QTextBrowser(self.DataRepository_tab)
        self.dr_tb_variables.setObjectName(u"dr_tb_variables")

        self.gridLayout_11.addWidget(self.dr_tb_variables, 1, 1, 3, 1)

        self.gridLayout_11.setRowStretch(0, 1)
        self.gridLayout_11.setRowStretch(1, 1)
        self.gridLayout_11.setRowStretch(2, 1)
        self.gridLayout_11.setRowStretch(3, 1)

        self.verticalLayout.addLayout(self.gridLayout_11)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.dr_cb_DT_browse = QComboBox(self.DataRepository_tab)
        self.dr_cb_DT_browse.setObjectName(u"dr_cb_DT_browse")

        self.gridLayout_13.addWidget(self.dr_cb_DT_browse, 0, 0, 3, 1)

        self.dr_pb_DT_browse = QPushButton(self.DataRepository_tab)
        self.dr_pb_DT_browse.setObjectName(u"dr_pb_DT_browse")
        self.dr_pb_DT_browse.setEnabled(False)
        self.dr_pb_DT_browse.setMinimumSize(QSize(100, 0))
        self.dr_pb_DT_browse.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_13.addWidget(self.dr_pb_DT_browse, 0, 1, 3, 1)

        self.gridLayout_13.setColumnStretch(0, 1)
        self.gridLayout_13.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout_13)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 6)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.dr_tb_console = QTextBrowser(self.DataRepository_tab)
        self.dr_tb_console.setObjectName(u"dr_tb_console")

        self.gridLayout_10.addWidget(self.dr_tb_console, 3, 1, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 1, 0, 2, 1)

        self.dr_pb_repo_drop = QPushButton(self.DataRepository_tab)
        self.dr_pb_repo_drop.setObjectName(u"dr_pb_repo_drop")
        self.dr_pb_repo_drop.setEnabled(True)
        self.dr_pb_repo_drop.setMinimumSize(QSize(200, 0))
        self.dr_pb_repo_drop.setMaximumSize(QSize(200, 16777215))
        self.dr_pb_repo_drop.setFlat(False)

        self.gridLayout_10.addWidget(self.dr_pb_repo_drop, 1, 1, 1, 2, Qt.AlignHCenter)

        self.gridLayout_10.setColumnStretch(0, 1)
        self.gridLayout_10.setColumnStretch(1, 1)
        self.gridLayout_10.setColumnStretch(2, 1)
        self.gridLayout_10.setColumnStretch(3, 1)

        self.verticalLayout_4.addLayout(self.gridLayout_10)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 10)
        self.verticalLayout_4.setStretch(2, 2)

        self.gridLayout_6.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.DataRepository_tab, "")
        self.DataExplorer = QWidget()
        self.DataExplorer.setObjectName(u"DataExplorer")
        self.horizontalLayout_13 = QHBoxLayout(self.DataExplorer)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.de_cb_data_pick_left = QComboBox(self.DataExplorer)
        self.de_cb_data_pick_left.setObjectName(u"de_cb_data_pick_left")

        self.verticalLayout_2.addWidget(self.de_cb_data_pick_left)

        self.de_tw_variables = QTableWidget(self.DataExplorer)
        self.de_tw_variables.setObjectName(u"de_tw_variables")

        self.verticalLayout_2.addWidget(self.de_tw_variables)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.de_sw_explorations = QStackedWidget(self.DataExplorer)
        self.de_sw_explorations.setObjectName(u"de_sw_explorations")
        self.UA_numeric = QWidget()
        self.UA_numeric.setObjectName(u"UA_numeric")
        self.horizontalLayout_8 = QHBoxLayout(self.UA_numeric)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.de_fr_plot = QFrame(self.UA_numeric)
        self.de_fr_plot.setObjectName(u"de_fr_plot")
        self.de_fr_plot.setFrameShape(QFrame.StyledPanel)
        self.de_fr_plot.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.de_fr_plot)

        self.de_cb_plot_selector = QComboBox(self.UA_numeric)
        self.de_cb_plot_selector.setObjectName(u"de_cb_plot_selector")

        self.verticalLayout_12.addWidget(self.de_cb_plot_selector)


        self.horizontalLayout_4.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.de_tw_quartiles = QTableWidget(self.UA_numeric)
        self.de_tw_quartiles.setObjectName(u"de_tw_quartiles")

        self.horizontalLayout_6.addWidget(self.de_tw_quartiles)

        self.de_tw_decils = QTableWidget(self.UA_numeric)
        self.de_tw_decils.setObjectName(u"de_tw_decils")

        self.horizontalLayout_6.addWidget(self.de_tw_decils)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_13.addLayout(self.horizontalLayout_6)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_11 = QLabel(self.UA_numeric)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 0, 0, 1, 1, Qt.AlignBottom)

        self.label_12 = QLabel(self.UA_numeric)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_7.addWidget(self.label_12, 2, 0, 1, 1, Qt.AlignBottom)

        self.label_13 = QLabel(self.UA_numeric)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_7.addWidget(self.label_13, 2, 1, 1, 1, Qt.AlignBottom)

        self.de_le_median_2 = QLineEdit(self.UA_numeric)
        self.de_le_median_2.setObjectName(u"de_le_median_2")
        self.de_le_median_2.setReadOnly(True)

        self.gridLayout_7.addWidget(self.de_le_median_2, 1, 1, 1, 1)

        self.label_14 = QLabel(self.UA_numeric)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_7.addWidget(self.label_14, 0, 1, 1, 1, Qt.AlignBottom)

        self.de_le_min_2 = QLineEdit(self.UA_numeric)
        self.de_le_min_2.setObjectName(u"de_le_min_2")
        self.de_le_min_2.setReadOnly(True)

        self.gridLayout_7.addWidget(self.de_le_min_2, 3, 0, 1, 1)

        self.de_le_mean_2 = QLineEdit(self.UA_numeric)
        self.de_le_mean_2.setObjectName(u"de_le_mean_2")
        self.de_le_mean_2.setReadOnly(True)

        self.gridLayout_7.addWidget(self.de_le_mean_2, 1, 0, 1, 1)

        self.label_15 = QLabel(self.UA_numeric)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_7.addWidget(self.label_15, 4, 0, 1, 1, Qt.AlignBottom)

        self.label_16 = QLabel(self.UA_numeric)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_7.addWidget(self.label_16, 4, 1, 1, 1, Qt.AlignBottom)

        self.de_le_max_2 = QLineEdit(self.UA_numeric)
        self.de_le_max_2.setObjectName(u"de_le_max_2")
        self.de_le_max_2.setReadOnly(True)

        self.gridLayout_7.addWidget(self.de_le_max_2, 3, 1, 1, 1)

        self.de_le_std_2 = QLineEdit(self.UA_numeric)
        self.de_le_std_2.setObjectName(u"de_le_std_2")
        self.de_le_std_2.setReadOnly(True)

        self.gridLayout_7.addWidget(self.de_le_std_2, 5, 0, 1, 1)

        self.de_le_nan_2 = QLineEdit(self.UA_numeric)
        self.de_le_nan_2.setObjectName(u"de_le_nan_2")
        self.de_le_nan_2.setReadOnly(True)

        self.gridLayout_7.addWidget(self.de_le_nan_2, 5, 1, 1, 1)


        self.verticalLayout_13.addLayout(self.gridLayout_7)

        self.verticalLayout_13.setStretch(0, 2)
        self.verticalLayout_13.setStretch(1, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_13)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 2)

        self.horizontalLayout_8.addLayout(self.horizontalLayout_4)

        self.de_sw_explorations.addWidget(self.UA_numeric)
        self.UA_character = QWidget()
        self.UA_character.setObjectName(u"UA_character")
        self.horizontalLayout_7 = QHBoxLayout(self.UA_character)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.de_fr_pie = QFrame(self.UA_character)
        self.de_fr_pie.setObjectName(u"de_fr_pie")
        self.de_fr_pie.setFrameShape(QFrame.StyledPanel)
        self.de_fr_pie.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.de_fr_pie)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.de_le_uniqs = QLineEdit(self.UA_character)
        self.de_le_uniqs.setObjectName(u"de_le_uniqs")

        self.gridLayout_5.addWidget(self.de_le_uniqs, 2, 1, 1, 1)

        self.label_2 = QLabel(self.UA_character)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 1, 1, 1, 1, Qt.AlignBottom)

        self.de_tw_freqs = QTableWidget(self.UA_character)
        self.de_tw_freqs.setObjectName(u"de_tw_freqs")

        self.gridLayout_5.addWidget(self.de_tw_freqs, 1, 0, 2, 1)

        self.de_fr_bar = QFrame(self.UA_character)
        self.de_fr_bar.setObjectName(u"de_fr_bar")
        self.de_fr_bar.setFrameShape(QFrame.StyledPanel)
        self.de_fr_bar.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.de_fr_bar, 0, 0, 1, 2)

        self.gridLayout_5.setRowStretch(0, 1)
        self.gridLayout_5.setRowStretch(1, 1)
        self.gridLayout_5.setRowStretch(2, 1)

        self.horizontalLayout_3.addLayout(self.gridLayout_5)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)

        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)

        self.de_sw_explorations.addWidget(self.UA_character)
        self.BA_num_vs_num = QWidget()
        self.BA_num_vs_num.setObjectName(u"BA_num_vs_num")
        self.horizontalLayout_10 = QHBoxLayout(self.BA_num_vs_num)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(35, -1, 35, -1)
        self.de_ba_corr_cb = QComboBox(self.BA_num_vs_num)
        self.de_ba_corr_cb.setObjectName(u"de_ba_corr_cb")

        self.verticalLayout_11.addWidget(self.de_ba_corr_cb, 0, Qt.AlignVCenter)

        self.label_7 = QLabel(self.BA_num_vs_num)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_11.addWidget(self.label_7)

        self.de_le_shifts = QLineEdit(self.BA_num_vs_num)
        self.de_le_shifts.setObjectName(u"de_le_shifts")

        self.verticalLayout_11.addWidget(self.de_le_shifts)

        self.label_8 = QLabel(self.BA_num_vs_num)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_11.addWidget(self.label_8)

        self.de_lw_columns = QListWidget(self.BA_num_vs_num)
        self.de_lw_columns.setObjectName(u"de_lw_columns")

        self.verticalLayout_11.addWidget(self.de_lw_columns)

        self.label_6 = QLabel(self.BA_num_vs_num)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_11.addWidget(self.label_6)

        self.de_le_corr = QLineEdit(self.BA_num_vs_num)
        self.de_le_corr.setObjectName(u"de_le_corr")
        self.de_le_corr.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.de_le_corr)

        self.verticalLayout_11.setStretch(0, 1)

        self.verticalLayout_10.addLayout(self.verticalLayout_11)

        self.de_fr_scatter = QFrame(self.BA_num_vs_num)
        self.de_fr_scatter.setObjectName(u"de_fr_scatter")
        self.de_fr_scatter.setFrameShape(QFrame.StyledPanel)
        self.de_fr_scatter.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.de_fr_scatter)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 1)

        self.horizontalLayout_9.addLayout(self.verticalLayout_10)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.de_fr_crosscorr = QFrame(self.BA_num_vs_num)
        self.de_fr_crosscorr.setObjectName(u"de_fr_crosscorr")
        self.de_fr_crosscorr.setFrameShape(QFrame.StyledPanel)
        self.de_fr_crosscorr.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.de_fr_crosscorr)

        self.de_fr_heatmap = QFrame(self.BA_num_vs_num)
        self.de_fr_heatmap.setObjectName(u"de_fr_heatmap")
        self.de_fr_heatmap.setFrameShape(QFrame.StyledPanel)
        self.de_fr_heatmap.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.de_fr_heatmap)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 1)

        self.horizontalLayout_9.addLayout(self.verticalLayout_9)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)

        self.de_sw_explorations.addWidget(self.BA_num_vs_num)
        self.BA_num_vs_char = QWidget()
        self.BA_num_vs_char.setObjectName(u"BA_num_vs_char")
        self.horizontalLayout_5 = QHBoxLayout(self.BA_num_vs_char)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.de_ba_nc_table = QTableWidget(self.BA_num_vs_char)
        self.de_ba_nc_table.setObjectName(u"de_ba_nc_table")

        self.horizontalLayout_11.addWidget(self.de_ba_nc_table)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.de_ba_nc_chart = QFrame(self.BA_num_vs_char)
        self.de_ba_nc_chart.setObjectName(u"de_ba_nc_chart")
        self.de_ba_nc_chart.setFrameShape(QFrame.StyledPanel)
        self.de_ba_nc_chart.setFrameShadow(QFrame.Raised)

        self.gridLayout_8.addWidget(self.de_ba_nc_chart, 1, 0, 1, 1)

        self.de_ba_nc_picker = QListWidget(self.BA_num_vs_char)
        self.de_ba_nc_picker.setObjectName(u"de_ba_nc_picker")

        self.gridLayout_8.addWidget(self.de_ba_nc_picker, 0, 0, 1, 1)

        self.gridLayout_8.setRowStretch(0, 1)
        self.gridLayout_8.setRowStretch(1, 4)

        self.horizontalLayout_11.addLayout(self.gridLayout_8)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 1)

        self.horizontalLayout_5.addLayout(self.horizontalLayout_11)

        self.de_sw_explorations.addWidget(self.BA_num_vs_char)
        self.BA_cat_vs_cat = QWidget()
        self.BA_cat_vs_cat.setObjectName(u"BA_cat_vs_cat")
        self.gridLayout_16 = QGridLayout(self.BA_cat_vs_cat)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_9 = QLabel(self.BA_cat_vs_cat)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_6.addWidget(self.label_9)

        self.de_ba_cc_chi2 = QLineEdit(self.BA_cat_vs_cat)
        self.de_ba_cc_chi2.setObjectName(u"de_ba_cc_chi2")
        self.de_ba_cc_chi2.setEnabled(False)

        self.verticalLayout_6.addWidget(self.de_ba_cc_chi2)


        self.gridLayout_14.addLayout(self.verticalLayout_6, 2, 0, 1, 2)

        self.de_ba_cc_stackedBars = QFrame(self.BA_cat_vs_cat)
        self.de_ba_cc_stackedBars.setObjectName(u"de_ba_cc_stackedBars")
        self.de_ba_cc_stackedBars.setFrameShape(QFrame.StyledPanel)
        self.de_ba_cc_stackedBars.setFrameShadow(QFrame.Raised)

        self.gridLayout_14.addWidget(self.de_ba_cc_stackedBars, 0, 1, 2, 1)

        self.de_ba_cc_crosstab = QFrame(self.BA_cat_vs_cat)
        self.de_ba_cc_crosstab.setObjectName(u"de_ba_cc_crosstab")
        self.de_ba_cc_crosstab.setFrameShape(QFrame.StyledPanel)
        self.de_ba_cc_crosstab.setFrameShadow(QFrame.Raised)

        self.gridLayout_14.addWidget(self.de_ba_cc_crosstab, 0, 0, 2, 1)

        self.gridLayout_14.setRowStretch(0, 8)
        self.gridLayout_14.setColumnStretch(0, 1)
        self.gridLayout_14.setColumnStretch(1, 1)

        self.gridLayout_16.addLayout(self.gridLayout_14, 0, 0, 1, 1)

        self.de_sw_explorations.addWidget(self.BA_cat_vs_cat)
        self.TableBrowser = QWidget()
        self.TableBrowser.setObjectName(u"TableBrowser")
        self.gridLayout_18 = QGridLayout(self.TableBrowser)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tb_tw = QTableWidget(self.TableBrowser)
        self.tb_tw.setObjectName(u"tb_tw")
        self.tb_tw.setAlternatingRowColors(True)

        self.horizontalLayout_15.addWidget(self.tb_tw)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_10 = QLabel(self.TableBrowser)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_17.addWidget(self.label_10, 1, 0, 1, 1)

        self.de_tb_le_buffer = QLineEdit(self.TableBrowser)
        self.de_tb_le_buffer.setObjectName(u"de_tb_le_buffer")

        self.gridLayout_17.addWidget(self.de_tb_le_buffer, 1, 1, 1, 1)

        self.de_tb_le_sorting = QLineEdit(self.TableBrowser)
        self.de_tb_le_sorting.setObjectName(u"de_tb_le_sorting")

        self.gridLayout_17.addWidget(self.de_tb_le_sorting, 0, 1, 1, 1)

        self.label_17 = QLabel(self.TableBrowser)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_17.addWidget(self.label_17, 0, 0, 1, 1)

        self.de_tb_pb_refresh = QPushButton(self.TableBrowser)
        self.de_tb_pb_refresh.setObjectName(u"de_tb_pb_refresh")

        self.gridLayout_17.addWidget(self.de_tb_pb_refresh, 2, 0, 1, 2)


        self.horizontalLayout_15.addLayout(self.gridLayout_17)

        self.horizontalLayout_15.setStretch(0, 3)
        self.horizontalLayout_15.setStretch(1, 1)

        self.gridLayout_18.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)

        self.de_sw_explorations.addWidget(self.TableBrowser)

        self.gridLayout_4.addWidget(self.de_sw_explorations, 1, 0, 1, 3)

        self.de_pb_explore = QPushButton(self.DataExplorer)
        self.de_pb_explore.setObjectName(u"de_pb_explore")

        self.gridLayout_4.addWidget(self.de_pb_explore, 0, 2, 1, 1)

        self.de_cb_tools = QComboBox(self.DataExplorer)
        self.de_cb_tools.setObjectName(u"de_cb_tools")

        self.gridLayout_4.addWidget(self.de_cb_tools, 0, 0, 1, 1)

        self.de_sw_tools = QStackedWidget(self.DataExplorer)
        self.de_sw_tools.setObjectName(u"de_sw_tools")
        self.UA_tool = QWidget()
        self.UA_tool.setObjectName(u"UA_tool")
        self.verticalLayout_15 = QVBoxLayout(self.UA_tool)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.de_cb_UA_var = QComboBox(self.UA_tool)
        self.de_cb_UA_var.setObjectName(u"de_cb_UA_var")

        self.horizontalLayout_14.addWidget(self.de_cb_UA_var)

        self.de_cb_UA_role = QComboBox(self.UA_tool)
        self.de_cb_UA_role.setObjectName(u"de_cb_UA_role")

        self.horizontalLayout_14.addWidget(self.de_cb_UA_role)


        self.verticalLayout_15.addLayout(self.horizontalLayout_14)

        self.de_sw_tools.addWidget(self.UA_tool)
        self.BA_tool = QWidget()
        self.BA_tool.setObjectName(u"BA_tool")
        self.verticalLayout_17 = QVBoxLayout(self.BA_tool)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.de_cb_BA_var2 = QComboBox(self.BA_tool)
        self.de_cb_BA_var2.setObjectName(u"de_cb_BA_var2")

        self.gridLayout_9.addWidget(self.de_cb_BA_var2, 1, 0, 1, 1)

        self.de_cb_BA_role1 = QComboBox(self.BA_tool)
        self.de_cb_BA_role1.setObjectName(u"de_cb_BA_role1")

        self.gridLayout_9.addWidget(self.de_cb_BA_role1, 0, 2, 1, 1)

        self.de_cb_BA_var1 = QComboBox(self.BA_tool)
        self.de_cb_BA_var1.setObjectName(u"de_cb_BA_var1")

        self.gridLayout_9.addWidget(self.de_cb_BA_var1, 0, 0, 1, 1)

        self.de_cb_BA_role2 = QComboBox(self.BA_tool)
        self.de_cb_BA_role2.setObjectName(u"de_cb_BA_role2")

        self.gridLayout_9.addWidget(self.de_cb_BA_role2, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.gridLayout_9.setColumnStretch(0, 3)
        self.gridLayout_9.setColumnStretch(1, 1)
        self.gridLayout_9.setColumnStretch(2, 3)

        self.verticalLayout_17.addLayout(self.gridLayout_9)

        self.de_sw_tools.addWidget(self.BA_tool)
        self.TB_tool = QWidget()
        self.TB_tool.setObjectName(u"TB_tool")
        self.de_sw_tools.addWidget(self.TB_tool)

        self.gridLayout_4.addWidget(self.de_sw_tools, 0, 1, 1, 1)

        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 10)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 2)
        self.gridLayout_4.setColumnStretch(2, 1)

        self.horizontalLayout_2.addLayout(self.gridLayout_4)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 8)

        self.horizontalLayout_13.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.DataExplorer, "")

        self.horizontalLayout_12.addWidget(self.tabWidget)


        self.gridLayout_15.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.tabBarClicked.connect(MainWindow.change_size)
        self.dl_pb_load_data.clicked.connect(MainWindow.load_data)
        self.dl_pb_load_pickle.clicked.connect(MainWindow.load_pickle)
        self.dl_pb_clear.clicked.connect(MainWindow.clear_curr_DT)
        self.dl_pb_save_pickle.clicked.connect(MainWindow.save_DT)
        self.dl_pb_summary.clicked.connect(MainWindow.print_summary)
        self.dl_pb_save_repo.clicked.connect(MainWindow.add_DT_to_repo)
        self.dr_pb_repo_drop.clicked.connect(MainWindow.drop_repo)
        self.dr_pb_DT_add.clicked.connect(MainWindow.DR_add_DT_to_repo)
        self.dr_pb_DT_remove.clicked.connect(MainWindow.drop_DT_from_repo)
        self.dr_pb_DT_browse.clicked.connect(MainWindow.DR_browse_DT)
        self.tabWidget.currentChanged.connect(MainWindow.center_window)
        self.de_cb_data_pick_left.currentTextChanged.connect(MainWindow.DE_tab_list_variables)
        self.de_pb_explore.clicked.connect(MainWindow.DE_exploration)
        self.de_cb_tools.currentTextChanged.connect(MainWindow.DE_set_cbs_for_tool)
        self.de_cb_plot_selector.currentTextChanged.connect(MainWindow.DE_replot_)
        self.de_cb_BA_var1.currentTextChanged.connect(MainWindow.DE_BA_pop_var1_role)
        self.de_cb_BA_var2.currentTextChanged.connect(MainWindow.DE_BA_pop_var2_role)
        self.de_cb_UA_var.currentTextChanged.connect(MainWindow.DE_UA_populate_roles)
        self.de_cb_UA_role.currentTextChanged.connect(MainWindow.DE_set_UA_sw)
        self.de_cb_BA_role1.currentTextChanged.connect(MainWindow.DE_set_BA_sw)
        self.de_cb_BA_role2.currentTextChanged.connect(MainWindow.DE_set_BA_sw)
        self.de_tb_pb_refresh.clicked.connect(MainWindow.DE_TB_refresh)

        self.tabWidget.setCurrentIndex(2)
        self.dl_pb_load_pickle.setDefault(False)
        self.de_sw_explorations.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MLOps Platform Interface", None))
        self.dl_pb_clear.setText(QCoreApplication.translate("MainWindow", u"Clear loaded data", None))
        self.dl_pb_save_pickle.setText(QCoreApplication.translate("MainWindow", u"Pickle-save data", None))
        self.dl_pb_summary.setText(QCoreApplication.translate("MainWindow", u"Summary", None))
        self.dl_pb_save_repo.setText(QCoreApplication.translate("MainWindow", u"Save to Repository", None))
        self.dl_pb_load_pickle.setText(QCoreApplication.translate("MainWindow", u"Load Saved DT", None))
        self.dl_pb_load_data.setText(QCoreApplication.translate("MainWindow", u"Load Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DataLoader_tab), QCoreApplication.translate("MainWindow", u"DataLoader", None))
        self.dr_le_repo_loc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Repository's location ...", None))
        self.dr_pb_DT_remove.setText(QCoreApplication.translate("MainWindow", u"Drop a DataTable", None))
        self.dr_pb_DT_add.setText(QCoreApplication.translate("MainWindow", u"Add a DataTable", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data Summary", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Shapes", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Variables", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Datetime of registering", None))
        self.dr_pb_DT_browse.setText(QCoreApplication.translate("MainWindow", u"Get details", None))
        self.dr_pb_repo_drop.setText(QCoreApplication.translate("MainWindow", u"Drop the Repository", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DataRepository_tab), QCoreApplication.translate("MainWindow", u"DataRepository", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Mean value", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Min. value", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Max. value", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Median value", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Standard deviation", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Count of NaNs", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Count of unique values", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Cross-correlation's shifts", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Columns for a correlations' heatmap", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Correlation's value", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Chi-squared continqency value: (The lower chi2-cont is the more probable dependance is)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Obs buffer:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Sorting in\n"
"SQL syntax", None))
        self.de_tb_pb_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh!", None))
        self.de_pb_explore.setText(QCoreApplication.translate("MainWindow", u"Explore!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DataExplorer), QCoreApplication.translate("MainWindow", u"DataExplorer", None))
    # retranslateUi

