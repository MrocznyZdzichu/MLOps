from DataRepository import DataRepository
from DataLoader import DataLoader

class DR_Tab:
    def __init__(self, window, repo):
        self.window = window
        self.repo   = repo

    def initialize_tab(self):
        self.populate_cbs()
        if self.window.dr_cb_DT_pick.count() > 0:
            self.window.dr_pb_DT_remove.setEnabled(1)

    def drop_repo(self):
        try:
            self.repo.drop_repo()
        except:
            self.__log_on_console('The deletion of the Repository has failed')
        else:
            self.__log_on_console('The repository has been deleted.')

        self.populate_cbs()
        self.window.dr_pb_DT_remove.setDisabled(1)

    def add_table(self):
        self.__log_on_console('Initiating a data loading.')
        loader = DataLoader()
        try:
            data   = loader.load_saved_DT()
        except:
            self.__log_on_console('Data loading has failed.')
        else:
            try:
                self.repo.add_DataTable(data)
            except:
                self.__log_on_console('Data registering into the Repository has failed.')
            else:
                self.__log_on_console('Data has been registered.')
                self.window.dr_pb_DT_remove.setEnabled(1)

        self.populate_cbs()

    def drop_from_repo(self):
        dropped_DT = self.window.dr_cb_DT_pick.currentText()
        self.__log_on_console(f'Trying to delete the {dropped_DT}')

        try:
            self.repo.remove_DataTable(dropped_DT)
        except:
            self.__log_on_console('The deletion has failed.')
        else:
            self.__log_on_console('The DataTable has been deleted.')
            if len(self.repo.get_maintained_DTs()) == 0:
                self.window.dr_pb_DT_remove.setDisabled(1)
        self.populate_cbs()

    def __log_on_console(self, msg):
        self.window.dr_tb_console.append(msg)

    def populate_cbs(self):
        available_DTs = self.repo.get_maintained_DTs()
        self.window.dr_cb_DT_pick.clear()
        self.window.dr_cb_DT_browse.clear()
        self.window.dr_cb_DT_pick.addItems(available_DTs)
        self.window.dr_cb_DT_browse.addItems(available_DTs)
