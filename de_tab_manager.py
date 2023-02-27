import DataExplorer as DE
import DataRepository as DR
from PyQt5.QtWidgets import QTableWidgetItem
#de_tw_variables lista ze zmiennymi, typami oraz liczba nulli

import DataExplorer


class DE_Tab:
    def __init__(self, window, repo):
        self.window = window
        self.repo   = repo
        self.UA     = DE.UnivariateAnalysis()
        self.tools  = ['UnivariateAnalysis']
        self.DE     = DataExplorer.UnivariateAnalysis()

    def initialize_tab(self):
        pass
        self.populate_cbs_with_tables()
        self.__populate_exploration_tools()

    def populate_cbs_with_tables(self):
        tables = self.repo.get_maintained_DTs()

        self.window.de_cb_data_pick_left.clear()
        self.window.de_cb_data_pick_left.addItem('')
        self.window.de_cb_data_pick_left.addItems(tables)

    def populate_variables_table(self, selected_DT):
        types_dict = {
            "A numeric variable" : "Numeric"
            ,"A datetime variable" : "Datetime"
            ,"A character variable" : "Character"
        }
        headers = ("Variable's name", "Datatype", "Null count")

        if selected_DT != '':
            variables = self.repo.get_variables(DT_name=selected_DT)
            data = self.repo.get_DT(selected_DT)
            res_list  = []

            for var in variables:
                dtype       = self.UA.get_var_type(data, var)
                dtype       = types_dict[dtype]
                null_counts = self.UA.get_null_count(data, var)
                res_list.append([var, dtype, null_counts])

            col_count = 3
            row_count = len(variables)
            self.window.de_tw_variables.setRowCount(row_count)
            self.window.de_tw_variables.setColumnCount(col_count)
            for row in range(0, row_count):
                for col in range(0, col_count):
                    value = res_list[row][col]
                    item = QTableWidgetItem(str(value))
                    self.window.de_tw_variables.setItem(row, col, item)

            self.window.de_tw_variables.setHorizontalHeaderLabels(headers)
            self.window.de_tw_variables.resizeColumnsToContents()

        else:
            self.window.de_tw_variables.clearContents()
            self.window.de_tw_variables.setRowCount(0)
            self.window.de_tw_variables.setColumnCount(0)

    def set_cbs_for_tool(self, selected_tool):
        page_indices = {
            "UA_tool"  : 0
            ,"BA_tool" : 1
        }
        if selected_tool == 'UnivariateAnalysis':
            page = "UA_tool"

        else:
            page = "BA_tool"
        self.window.de_sw_tools.setCurrentIndex(page_indices[page])

    def populate_UA_cb(self):
        data = self.window.de_cb_data_pick_left.currentText()
        tool = self.window.de_cb_tools.currentText()

        if data != '' and tool == 'UnivariateAnalysis':
            variables = self.repo.get_variables(DT_name=data)
            self.window.de_cb_UA_var.clear()
            self.window.de_cb_UA_var.addItems(variables)

    def set_UA_sw(self, variable):
        if variable == '':
            return

        page_indices = {
            "numeric"    : 0
            ,"character" : 1
        }
        table_name = self.window.de_cb_data_pick_left.currentText()
        var_type   = self.__get_var_type(table_name, variable)

        page_idx = page_indices[var_type]
        if page_idx in (0, 1):
            self.window.de_sw_explorations.setCurrentIndex(page_idx)

    def exploration(self):
        DT_explored = self.window.de_cb_data_pick_left.currentText()
        variable    = self.window.de_cb_UA_var.currentText()

        if DT_explored == '':
            return

        DT   = self.repo.get_DT(DT_name=DT_explored)
        tool = self.window.de_cb_tools.currentText()
        if tool not in self.tools:
            return

        if tool == 'UnivariateAnalysis':
            variable = self.window.de_cb_UA_var.currentText()
            if variable == '':
                return

            var_type = self.__get_var_type(DT_explored, variable)
            if var_type == 'numeric':
                self.__UA_numeric(DT, variable)

    def __populate_exploration_tools(self):
        self.window.de_cb_tools.clear()
        self.window.de_cb_tools.addItem('')
        self.window.de_cb_tools.addItems(self.tools)

    def __get_var_type(self, table_name, variable):
        DT       = self.repo.get_DT(DT_name=table_name)
        var_type = self.DE.get_var_type(DT, variable)
        type_shorten = {
            "A numeric variable"    : "numeric"
            ,"A character variable" : "character"
        }
        return type_shorten[var_type]

    def __UA_numeric(self, DT, variable):
        mean   = self.DE.get_mean(DT, variable)
        median = self.DE.get_median(DT, variable)
        stddev = self.DE.get_stddev(DT, variable)
        min    = self.DE.get_min(DT, variable)
        max    = self.DE.get_max(DT, variable)
        nans   = self.DE.get_nan_count(DT, variable)

        self.window.de_le_mean_2.setText(str(mean))
        self.window.de_le_median_2.setText(str(median))
        self.window.de_le_nan_2.setText(str(nans))
        self.window.de_le_std_2.setText(str(stddev))
        self.window.de_le_min_2.setText(str(min))
        self.window.de_le_max_2.setText(str(max))

        quartiles = self.__compute_quartiles(DT, variable)
        self.__put_quartiles_into_tw(quartiles)
        decils    = self.__compute_decils(DT, variable)
        self.__put_decils_into_tw(decils)

        self.DE.plot_histogram(DT, variable, self.window.de_fr_histogram)
        self.DE.plot_boxplot(DT, variable, self.window.de_fr_boxplot)
        self.DE.plot_values(DT, variable, self.window.de_fr_serie)

    def __compute_quartiles(self, DT, variable):
        quartiles = []
        for i in range(0, 3):
            quartiles.append(self.DE.get_quantile(DT, variable, q=i*0.25))
        return quartiles

    def __put_quartiles_into_tw(self, quartiles):
        self.window.de_tw_quartiles.clearContents()
        self.window.de_tw_quartiles.setRowCount(3)
        self.window.de_tw_quartiles.setColumnCount(2)

        headers = ("No of quartile", "Quartile's value")
        self.window.de_tw_quartiles.setHorizontalHeaderLabels(headers)

        for i in range(0, 3):
            quartile_no    = i+1
            item = QTableWidgetItem(str(quartile_no))
            self.window.de_tw_quartiles.setItem(i, 0, item)

            quartile_value = quartiles[i]
            item = QTableWidgetItem(str(quartile_value))
            self.window.de_tw_quartiles.setItem(i, 1, item)

        self.window.de_tw_quartiles.resizeColumnsToContents()

    def __compute_decils(self, DT, variable):
        decils = []
        for i in range(0, 9):
            decils.append(self.DE.get_quantile(DT, variable, q=i*0.1))
        return decils

    def __put_decils_into_tw(self, decils):
        self.window.de_tw_decils.clearContents()
        self.window.de_tw_decils.setRowCount(9)
        self.window.de_tw_decils.setColumnCount(2)

        headers = ("No of a decile", "The decils's value")
        self.window.de_tw_decils.setHorizontalHeaderLabels(headers)

        for i in range(0, 9):
            decile_no    = i+1
            item = QTableWidgetItem(str(decile_no))
            self.window.de_tw_decils.setItem(i, 0, item)

            decile_value = decils[i]
            item = QTableWidgetItem(str(decile_value))
            self.window.de_tw_decils.setItem(i, 1, item)

        self.window.de_tw_decils.resizeColumnsToContents()
