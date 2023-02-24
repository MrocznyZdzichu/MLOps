from DataRepository import DataRepository
from DataLoader import DataLoader

class DR_Tab:
    def __init__(self, window, repo):
        self.window = window
        self.repo   = repo

    def initialize_tab(self):
        self.populate_cbs()
        self.switch_buttons()
        self.window.dr_le_repo_loc.setText(
            self.repo.get_deployment_dir()
        )

    def drop_repo(self):
        try:
            self.repo.drop_repo()
        except:
            self.__log_on_console('The deletion of the Repository has failed')
        else:
            self.__log_on_console('The repository has been deleted.')

        self.switch_buttons()
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

        self.switch_buttons()
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

        self.switch_buttons()
        self.populate_cbs()

    def browse_DT(self):
        selected_DT = self.window.dr_cb_DT_browse.currentText()
        tbs_texts = {
            self.window.dr_tb_summary        : self.repo.get_summaries(DT_name=selected_DT)
            ,self.window.dr_tb_variables     : self.__list_variables(selected_DT)
            ,self.window.dr_le_shapes        : self.__list_shapes(selected_DT)
            ,self.window.dr_le_register_dttm : str(self.repo.get_register_times(DT_name=selected_DT))
        }

        for textBrowser in tbs_texts.keys():
            textBrowser.setText(tbs_texts[textBrowser])

    def __log_on_console(self, msg):
        self.window.dr_tb_console.append(msg)

    def __list_variables(self, DT):
        variables = self.repo.get_variables(DT_name=DT)
        result = ""
        for var in variables:
            result += f"{var}\n"
        return result

    def __list_shapes(self, DT):
        shapes = self.repo.get_shapes(DT_name=DT)
        return f"{shapes[0]} rows vs. {shapes[1]} columns"

    def populate_cbs(self):
        available_DTs = self.repo.get_maintained_DTs()
        self.window.dr_cb_DT_pick.clear()
        self.window.dr_cb_DT_browse.clear()
        self.window.dr_cb_DT_pick.addItems(available_DTs)
        self.window.dr_cb_DT_browse.addItems(available_DTs)

    def switch_buttons(self):
        if len(self.repo.get_maintained_DTs()) > 0:
            self.window.dr_pb_DT_remove.setEnabled(1)
            self.window.dr_pb_DT_browse.setEnabled(1)
        else:
            self.window.dr_pb_DT_remove.setDisabled(1)
            self.window.dr_pb_DT_browse.setDisabled(1)
