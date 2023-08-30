import numpy as np
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

    def prepare_UI(self):
        self.__switch_explore_sw()
        self.__switch_tools_sw()
        self.__disable_explore_button()

    def refresh_exploration(self):
        table_name = GUI_utils.read_comboBox(self.__table_name_cb)
        if table_name == '':
            return
        
        buffer_length = self.__read_buffer_size()
        data = self.__repo.get_DT(table_name).get_core().head(buffer_length)
        data_numpy = np.array(data)
        GUI_utils.populate_tableWidget(
            self.__output_tw
            ,data_numpy
        )

    def buffer_changed_slot(self, buffer_text):
        try:
            buffer_length = int(buffer_text)
        except:
            self.__buffer_le.clear()
        else:
            self.refresh_exploration()
        

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