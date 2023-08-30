import DataLoader as DL
import DataRepository as DR
import GUI_utils


class DL_Tab:
    def __init__(self, window, repo):
        self.window = window
        self.loader = DL.DataLoader()
        self.repo   = repo

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
            self.__dl_log_msg('An error occured during loading the pickle')
        else:
            self.__dl_log_msg('Data loaded successfully')
            self.__dl_post_loading_pb_switch()

    def print_summary(self):
        summary_string = self.__curr_DT.get_summary()
        self.__dl_log_msg(summary_string)

    def save_DT(self):
        self.__dl_log_msg('Saving the DataTable')
        try:
            self.__curr_DT.save()
        except:
            self.__dl_log_msg('An error occured during saving the DataTable')
        else:
            self.__dl_log_msg('Saving successful')

    def clear_curr_DT(self):
        del self.__curr_DT
        self.__dl_log_msg('Current DataTable cleared')
        self.__dl_post_clearing_pb_switch()

    def add2repo(self):
        self.__dl_log_msg(f'Registering {self.__curr_DT.get_name()} DataTable into the Repository')
        try:
            self.repo.add_DataTable(self.__curr_DT)
        except:
            self.__dl_log_msg('Registering was unsuccessful :(')
        else:
            self.__dl_log_msg('The DataTable was registered successfully')

    def __dl_log_msg(self, msg):
        GUI_utils.textBrowser_append(self.window.dl_tb_log_console, msg)

    def __dl_post_loading_pb_switch(self):
        GUI_utils.disable_pushButton(self.window.dl_pb_load_data)
        GUI_utils.disable_pushButton(self.window.dl_pb_load_pickle)
        GUI_utils.enable_pushButton(self.window.dl_pb_clear)
        GUI_utils.enable_pushButton(self.window.dl_pb_save_pickle)
        GUI_utils.enable_pushButton(self.window.dl_pb_summary)
        GUI_utils.enable_pushButton(self.window.dl_pb_save_repo)

    def __dl_post_clearing_pb_switch(self):
        GUI_utils.enable_pushButton(self.window.dl_pb_load_data)
        GUI_utils.enable_pushButton(self.window.dl_pb_load_pickle)
        GUI_utils.disable_pushButton(self.window.dl_pb_clear)
        GUI_utils.disable_pushButton(self.window.dl_pb_save_pickle)
        GUI_utils.disable_pushButton(self.window.dl_pb_summary)
        GUI_utils.disable_pushButton(self.window.dl_pb_save_repo)
