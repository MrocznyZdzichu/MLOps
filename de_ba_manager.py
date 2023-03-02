import DataExplorer as DE
import GUI_utils

class BA_manager:
    def __init__(self, window, repo):
        self.window     = window
        self.repo       = repo
#        self.UA         = DE.BivariateAnalysis()

    def populate_BA_cbs(self):
        table_name = self.window.de_cb_data_pick_left.currentText()

        if table_name != '':
            variables = self.repo.get_variables(table_name)
            var1_cb = self.window.de_cb_BA_var1
            var2_cb = self.window.de_cb_BA_var2

            comboBoxes = (var1_cb, var2_cb)
            for cb in comboBoxes:
                GUI_utils.populate_comboBox(cb, variables)
