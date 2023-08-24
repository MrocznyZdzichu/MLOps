from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import DataExplorer as DE
import GUI_utils

class BA_manager:
    def __init__(self, window, repo):
        self.window     = window
        self.repo       = repo
        self.BA         = DE.BivariateAnalysis()

        self.var1_cb        = self.window.de_cb_BA_var1
        self.var2_cb        = self.window.de_cb_BA_var2
        self.table_name_cb  = self.window.de_cb_data_pick_left

        self.corr_method_cb = self.window.de_ba_corr_cb
        self.sw             = self.window.de_sw_explorations
        self.corr_le        = self.window.de_le_corr
        self.shifts_le      = self.window.de_le_shifts
        self.cross_corr_fr  = self.window.de_fr_crosscorr
        self.heatmap_fr     = self.window.de_fr_heatmap
        self.scatter_fr     = self.window.de_fr_scatter
        self.cols_lw        = self.window.de_lw_columns
        self.corr_methods   = ['pearson', 'spearman', 'kendall']

        self.uniq_vars_lw  = self.window.de_ba_nc_picker
        self.nc_table      = self.window.de_ba_nc_table
        self.nc_chart      = self.window.de_ba_nc_chart

    def populate_BA_cbs(self):
        table_name = self.__get_table_name()

        if table_name != '':
            variables = self.repo.get_variables(table_name)
            comboBoxes = (self.var1_cb, self.var2_cb)
            for cb in comboBoxes:
                GUI_utils.clear_comboBox(cb)
            for cb in comboBoxes:
                GUI_utils.populate_comboBox(cb, variables)

    def change_sw_page(self):
        var1, var2 = self.get_variables()
        tool = self.__get_tool()

        if var1 != '' and var2 != '' and tool == 'BivariateAnalysis':
            types_pages = {
                'num_vs_num'    : 2
                ,'num_vs_char'  : 3
            }
            types = self.__get_types()
            analysis_type = ''

            if 'A datetime variable' in types:
                return

            if all(vartype == 'A numeric variable' for vartype in types):
                analysis_type = 'num_vs_num'
                GUI_utils.populate_comboBox(self.corr_method_cb, self.corr_methods)

            if any(vartype == 'A numeric variable' for vartype in types) and any(vartype == 'A character variable' for vartype in types):
                analysis_type = 'num_vs_char'
                char_var_name = var1 if types[0] == 'A character variable' else var2
                self.populate_BA_nc_lw(self.__get_table_name(), char_var_name)

            if analysis_type in types_pages.keys():
                GUI_utils.change_stackedWidget_page(self.sw, types_pages[analysis_type])

    def populate_BA_lw(self, DT_name):
        GUI_utils.clear_listWidget(self.cols_lw)
        if DT_name == '':
            return

        column_names = self.repo.get_variables(DT_name)
        GUI_utils.populate_listWidget(self.cols_lw, column_names)

    def populate_BA_nc_lw(self, DT_name, char_var):
        GUI_utils.clear_listWidget(self.uniq_vars_lw)
        if DT_name == '':
            return

        DT = self.repo.get_DT(DT_name)
        uniq_vars = list(DT.get_core()[char_var].unique())
        GUI_utils.populate_listWidget(self.uniq_vars_lw, uniq_vars)

    def explore(self, DT_name, DT, var1, var2):
        types = self.__get_types()
        if all(vartype == 'A numeric variable' for vartype in types):
            self.__num_vs_num_explore(DT_name, DT, var1, var2)

    def __get_table_name(self):
        return self.table_name_cb.currentText()

    def get_variables(self):
        return self.window.de_cb_BA_var1.currentText(), \
                self.window.de_cb_BA_var2.currentText()

    def __get_types(self):
        var1, var2 = self.get_variables()
        DT = self.repo.get_DT(self.__get_table_name())

        types = [
            DE.get_var_type(DT, var1)
            ,DE.get_var_type(DT, var2)
        ]
        return types

    def __get_tool(self):
        return self.window.de_cb_tools.currentText()

    def __get_corr_type(self):
        return self.corr_method_cb.currentText()

    def __num_vs_num_explore(self, DT_name, DT, var1, var2):
        method = self.__get_corr_type()

        corr = self.BA.get_correlation(DT, var1, var2, method=method)
        GUI_utils.set_lineEdit_text(self.corr_le, str(corr))

        self.BA.plot_scatterplot(DT, var1, var2, widget=self.scatter_fr)

        cols_subset = []
        for i in range(self.cols_lw.count()):
            item = self.cols_lw.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                cols_subset.append(item.text())

        if len(cols_subset) == 0:
            cols_subset = None

        self.BA.plot_corr_heatmap(DT, cols=cols_subset,
                                widget=self.heatmap_fr, method=method)


        shifts_input = self.shifts_le.text()
        try:
            int(shifts_input)
        except:
            n_shifts = None
            GUI_utils.clear_lineEdit(self.shifts_le)
        else:
            n_shifts = int(shifts_input)

        self.BA.plot_crosscorrelation(DT, var1, var2,
                                    n_shifts=n_shifts,
                                    norm=True,
                                    widget=self.cross_corr_fr)
