import DataExplorer as DE
import DataRepository as DR
from PyQt5.QtWidgets import QTableWidgetItem

import DataExplorer
import GUI_utils
from de_ua_manager import UA_manager
from de_ba_manager import BA_manager


class DE_Tab:
    def __init__(self, window, repo):
        self.window = window
        self.repo   = repo
        self.tools  = ['UnivariateAnalysis', 'BivariateAnalysis']

        self.UA_manager = UA_manager(window, repo)
        self.BA_manager = BA_manager(window, repo)

    def initialize_tab(self):
        self.__populate_cbs_with_tables()
        self.__populate_exploration_tools()
        self.UA_manager.populate_cb_UA_num_plot()

    def populate_variables_table(self, selected_DT):
        types_dict = {
            "A numeric variable" : "Numeric"
            ,"A datetime variable" : "Datetime"
            ,"A character variable" : "Character"
        }
        headers = ("Variable's name", "Datatype", "Null count")
        columns_table = self.window.de_tw_variables

        if selected_DT != '':
            variables = self.repo.get_variables(DT_name=selected_DT)
            data = self.repo.get_DT(selected_DT)
            res_list  = []

            for var in variables:
                dtype       = DE.get_var_type(data, var)
                dtype       = types_dict[dtype]
                null_counts = self.UA_manager.UA.get_null_count(data, var)
                res_list.append([var, dtype, null_counts])

            GUI_utils.populate_tableWidget(columns_table,
                                            res_list,
                                            headers)
        else:
            GUI_utils.clear_tableWidget(columns_table)

    def set_cbs_for_tool(self, selected_tool):
        page_indices = {
            "UA_tool"  : 0
            ,"BA_tool" : 1
        }
        if selected_tool == 'UnivariateAnalysis':
            page = "UA_tool"

        else:
            page = "BA_tool"
        tools_config = self.window.de_sw_tools
        GUI_utils.change_stackedWidget_page(tools_config, page_indices[page])

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
            self.UA_manager.UnivariateExploration(DT_explored
                                                 ,DT
                                                 ,variable)
        elif tool == 'BivariateAnalysis':
            var1, var2 = self.BA_manager.get_variables()
            if var1 != '' and var2 != '':
                self.BA_manager.explore(DT_explored
                                        ,DT
                                        ,var1
                                        ,var2)

    def __populate_cbs_with_tables(self):
        tables         = self.repo.get_maintained_DTs()
        table_selector = self.window.de_cb_data_pick_left

        GUI_utils.populate_comboBox(table_selector, tables, empty_first=1)

    def __populate_exploration_tools(self):
        tool_selector = self.window.de_cb_tools
        GUI_utils.populate_comboBox(tool_selector, self.tools)
