import DataLoader as DL
import DataRepository as DR

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

    def __dl_log_msg(self, msg):
        self.window.dl_tb_log_console.append(msg)

    def __dl_post_loading_pb_switch(self):
        self.window.dl_pb_load_data.setDisabled(1)
        self.window.dl_pb_load_pickle.setDisabled(1)
        self.window.dl_pb_clear.setEnabled(1)
        self.window.dl_pb_save_pickle.setEnabled(1)
        self.window.dl_pb_summary.setEnabled(1)
        self.window.dl_pb_save_repo.setEnabled(1)

    def clear_curr_DT(self):
        del self.__curr_DT
        self.__dl_log_msg('Current DataTable cleared')
        self.__dl_post_clearing_pb_switch()

    def __dl_post_clearing_pb_switch(self):
        self.window.dl_pb_load_data.setEnabled(1)
        self.window.dl_pb_load_pickle.setEnabled(1)
        self.window.dl_pb_clear.setDisabled(1)
        self.window.dl_pb_save_pickle.setDisabled(1)
        self.window.dl_pb_summary.setDisabled(1)
        self.window.dl_pb_save_repo.setDisabled(1)

    def add2repo(self):
        self.__dl_log_msg(f'Registering {self.__curr_DT.get_name()} DataTable into the Repository')
        try:
            self.repo.add_DataTable(self.__curr_DT)
        except:
            self.__dl_log_msg('Registering was unsuccessful :(')
        else:
            self.__dl_log_msg('The DataTable was registered successfully')
