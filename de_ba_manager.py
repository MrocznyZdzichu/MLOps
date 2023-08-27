from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np

import DataExplorer as DE
import GUI_utils

class BA_manager:
    def __init__(self, window, repo):
        self.window     = window
        self.repo       = repo
        self.BA         = DE.BivariateAnalysis()

        self.variables_roles = {
            'A numeric variable'    : ['Values', 'Categories']
            ,'A character variable' : ['Categories']
        }
        self.var1_cb        = self.window.de_cb_BA_var1
        self.var2_cb        = self.window.de_cb_BA_var2
        self.var1_role_cb   = self.window.de_cb_BA_role1
        self.var2_role_cb   = self.window.de_cb_BA_role2
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
        var1, var2  = self.get_variables()
        role1, role2 = self.__get_roles()
        tool        = self.__get_tool()

        if var1 != '' and var2 != '' \
        and tool == 'BivariateAnalysis' \
        and role1 != '' and role2 != '':
            types_pages = {
                'num_vs_num'    : 2
                ,'num_vs_char'  : 3
            }
            analysis_type = ''
            if role1 == 'Values' and role2 == 'Values':
                analysis_type = 'num_vs_num'
                GUI_utils.populate_comboBox(
                    self.corr_method_cb
                    , self.corr_methods
                )

            if any(role == 'Categories' for role in (role1, role2))  \
            and any(role == 'Values' for role in (role1, role2)):
                analysis_type = 'num_vs_char'
                char_var_name = self.__get_char_variable()
                self.populate_BA_nc_lw(self.__get_table_name(), char_var_name)

            if analysis_type in types_pages.keys():
                GUI_utils.change_stackedWidget_page(self.sw, types_pages[analysis_type])

    def populate_var_role_cb1(self, variable):
        var_type = self.__get_types(variable=variable)
        GUI_utils.populate_comboBox(
            self.var1_role_cb
            , self.variables_roles[var_type]
        )

    def populate_var_role_cb2(self, variable):
        var_type = self.__get_types(variable=variable)
        GUI_utils.populate_comboBox(
            self.var2_role_cb
            , self.variables_roles[var_type]
        )


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
        uniq_vars = list(DT.get_core()[char_var].astype(str).unique())
        GUI_utils.populate_listWidget(self.uniq_vars_lw, uniq_vars)

    def explore(self, DT_name, DT, var1, var2):
        role1, role2 = self.__get_roles()
        if role1 == 'Values' and role2 == 'Values':
            self.__num_vs_num_explore(DT_name, DT, var1, var2)
            
        if any(role == 'Categories' for role in (role1, role2))  \
        and any(role == 'Values' for role in (role1, role2)):
            self.__num_vs_char_explore(DT_name, DT, var1, var2)

    def __get_table_name(self):
        return self.table_name_cb.currentText()

    def get_variables(self):
        return self.window.de_cb_BA_var1.currentText(), \
                self.window.de_cb_BA_var2.currentText()
    
    def __get_roles(self):
        role1 = self.var1_role_cb.currentText()
        role2 = self.var2_role_cb.currentText()
        return [role1, role2]
    
    def __get_types(self, variable=''):
        DT = self.repo.get_DT(self.__get_table_name())
        if variable == '':
            var1, var2 = self.get_variables()
            types = [
                DE.get_var_type(DT, var1)
                ,DE.get_var_type(DT, var2)
            ]
        else:
            types = DE.get_var_type(DT, variable)
        return types

    def __get_tool(self):
        return self.window.de_cb_tools.currentText()

    def __get_corr_type(self):
        return self.corr_method_cb.currentText()

    def __get_char_variable(self):
        var1, var2 = self.get_variables()
        types = self.__get_types()
        char_var_name = var1 if types[0] == 'A character variable' else var2
        return char_var_name
    
    def __num_vs_num_explore(self, DT_name, DT, var1, var2):
        method = self.__get_corr_type()

        corr = self.BA.get_correlation(DT, var1, var2, method=method)
        GUI_utils.set_lineEdit_text(self.corr_le, str(corr))

        self.BA.plot_scatterplot(DT, var1, var2, widget=self.scatter_fr)

        cols_subset = GUI_utils.get_lw_items(self.cols_lw)

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

    def __num_vs_char_explore(self, DT_name, DT, var1, var2):
        char_var_name = self.__get_char_variable()
        num_var_name  = var1 if var1 != char_var_name else var2

        group_stats, headers = self.__stats_in_group_preparation(
            DT, 
            num_var_name, 
            char_var_name
        )
        
        GUI_utils.populate_tableWidget(
            self.nc_table, 
            np.array(group_stats), 
            headers
        )

        classes = GUI_utils.get_lw_items(self.uniq_vars_lw)
        self.BA.plot_distribution_by_group(
            DT, 
            char_var_name, 
            num_var_name, 
            widget=self.nc_chart,
            filter=classes
        )

    def __stats_in_group_preparation(self, DT, num_var_name, char_var_name):
        group_stats = self.BA.num_stats_in_groups(
            DT, 
            num_var_name, 
            char_var_name
        ).round(3)

        group_stats.reset_index(inplace=True)
        group_stats.rename(columns={'index': 'Grouping Value'}, inplace=True)
        group_stats = group_stats.rename(columns={
            'mean': 'Mean',
            'median': 'Median',
            'std': 'Standard Deviation',
            'min': 'Min',
            'max': 'Max',
            'count': 'Count',
            'nunique': 'Unique Values'
        })
        headers = []
        for stat_name in list(group_stats.columns):
            headers.append(stat_name[1])        
        
        # Add the grouping column
        headers[0] = char_var_name

        return group_stats, headers