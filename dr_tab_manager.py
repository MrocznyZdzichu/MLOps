from DataRepository import DataRepository
from DataLoader import DataLoader

class DR_Tab:
    def __init__(self, window, repo):
        self.window = window
        self.repo   = repo

    def initialize_tab(self):
        self.populate_cbs()

    def drop_repo(self):
        try:
            self.repo.drop_repo()
        except:
            self.__log_on_console('The deletion of the Repository has failed')
        else:
            self.__log_on_console('The repository has been deleted.')

        self.populate_cbs()

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

        self.populate_cbs()

    def __log_on_console(self, msg):
        self.window.dr_tb_console.append(msg)

    def populate_cbs(self):
        available_DTs = self.repo.get_maintained_DTs()
        self.window.dr_cb_DT_pick.clear()
        self.window.dr_cb_DT_browse.clear()
        self.window.dr_cb_DT_pick.addItems(available_DTs)
        self.window.dr_cb_DT_browse.addItems(available_DTs)
