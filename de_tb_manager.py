import numpy as np
from functools import partial
from PyQt5 import QtCore

import GUI_utils


class TableBrowserManager:
    def __init__(self, window, repo):
        self.__repo = repo
        self.__table_browser_sw_idx = 5
        self.__tools_sw_idx         = 2
        
        self.__default_buffer   = 200
        
        self.__tab_sw       = window.de_sw_explorations
        self.__tools_sw     = window.de_sw_tools
        self.__explore_pb   = window.de_pb_explore

        self.__table_name_cb    = window.de_cb_data_pick_left
        self.__output_tw        = window.tb_tw
        self.__buffer_le        = window.de_tb_le_buffer
        self.__sorting_le       = window.de_tb_le_sorting

        self.__cols_sorting = {}
        
    def prepare_UI(self):
        self.__switch_explore_sw()
        self.__switch_tools_sw()
        self.__disable_explore_button()

    def reset_params(self):
        self.__cols_sorting = {}
        for widget in (self.__buffer_le, self.__sorting_le):
            GUI_utils.set_lineEdit_text(widget, '')

    def refresh_exploration(self):
        self.__update_sorting()

        table_name = self.__get_table_name()
        if table_name == '':
            return
        
        DT = self.__repo.get_DT(table_name)

        data = self.__process_DT(DT)
        data_numpy = np.array(data)

        columns = list(data.columns)
        self.__data_columns = columns

        GUI_utils.populate_tableWidget(
            self.__output_tw
            ,data_numpy
            ,columns
        )

    def __get_table_name(self):
        return GUI_utils.read_comboBox(self.__table_name_cb)
    
    def __switch_explore_sw(self):
        GUI_utils.change_stackedWidget_page(
            self.__tab_sw
            , self.__table_browser_sw_idx
        )

    def __switch_tools_sw(self):
        GUI_utils.change_stackedWidget_page(
            self.__tools_sw
            ,self.__tools_sw_idx
        )

    def __disable_explore_button(self):
        GUI_utils.disable_pushButton(self.__explore_pb)

    def __read_buffer_size(self):
        buffer_text = GUI_utils.read_lineEdit(self.__buffer_le)
        if buffer_text == '':
            return self.__default_buffer
        
        try:
            buffer_length = int(buffer_text)
        except ValueError:
            return self.__default_buffer
        
        return int(buffer_length)

    def __update_sorting(self):
        self.__cols_sorting = {}
        sort_text_input = GUI_utils.read_lineEdit(self.__sorting_le)

        if self.__validate_sorting_string(sort_text_input) == False:
            return

    def __validate_sorting_string(self, sorting_text):
        if sorting_text == '':
            return False
        text_parsed = sorting_text.replace(' ,', ',')
        text_parsed = sorting_text.replace(', ', ',')
        text_parsed = text_parsed.split(',')
                
        col_names, do_ascs = self.__prepare_sorting_lists(text_parsed)

        if all(sort_col in self.__data_columns for sort_col in col_names):
            for i in range(0, len(col_names)):
                self.__cols_sorting[col_names[i]] = do_ascs[i]
            return True
        else:
            return False
        
    def __prepare_sorting_lists(self, parsed_sorting_text):
        col_names = []
        do_ascs  = []

        for col in parsed_sorting_text:
            if len(col) > 4:
                if col[-4:].lower() == 'desc':
                    col_names.append(col[:-4])
                    do_ascs.append(False)
                else:
                    col_names.append(col)
                    do_ascs.append(True)
            else:
                col_names.append(col)
                do_ascs.append(True)

        return col_names, do_ascs
    
    def __process_DT(self, DT):
        buffer_length = self.__read_buffer_size()
        if self.__cols_sorting == {}:
            data = DT.get_core()
        else:
            data = DT.sort(self.__cols_sorting)

        return data.head(buffer_length)