import DataExplorer as DE
import GUI_utils


class UA_manager:
    def __init__(self, window, repo):
        self.window     = window
        self.repo       = repo
        self.UA         = DE.UnivariateAnalysis()
        self.plot_types = ['Histogram', 'Boxplot', "Values' chart"]

    def populate_cb_UA_num_plot(self):
        plot_selector = self.window.de_cb_plot_selector
        GUI_utils.populate_comboBox(plot_selector, self.plot_types)

    def populate_UA_cb(self):
        data = self.window.de_cb_data_pick_left.currentText()
        tool = self.window.de_cb_tools.currentText()

        if data != '' and tool == 'UnivariateAnalysis':
            variables       = self.repo.get_variables(DT_name=data)
            UA_var_selector = self.window.de_cb_UA_var

            GUI_utils.populate_comboBox(UA_var_selector, variables)

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
            UA_stackedWidget = self.window.de_sw_explorations
            GUI_utils.change_stackedWidget_page(UA_stackedWidget
                                                ,page_idx)

    def UnivariateExploration(self, DT_name, DT, variable):
        var_type = self.__get_var_type(DT_name, variable)
        if var_type == 'numeric':
            self.__numeric_exploration(DT, variable)
        elif var_type == 'character':
            self.__character_exploration(DT, variable)

    def replot_numeric(self, plot_type):
        DT_name = self.window.de_cb_data_pick_left.currentText()
        if DT_name == '':
            return

        DT = self.repo.get_DT(DT_name)

        var = self.window.de_cb_UA_var.currentText()
        if var == '':
            return

        self.__generate_numeric_plot(DT, var, self.window.de_fr_plot, plot_type)

    def __get_var_type(self, table_name, variable):
        DT       = self.repo.get_DT(DT_name=table_name)
        var_type = self.UA.get_var_type(DT, variable)
        type_shorten = {
            "A numeric variable"    : "numeric"
            ,"A character variable" : "character"
        }
        return type_shorten[var_type]

    def __numeric_exploration(self, DT, variable):
        mean   = self.UA.get_mean(DT, variable)
        median = self.UA.get_median(DT, variable)
        stddev = self.UA.get_stddev(DT, variable)
        min    = self.UA.get_min(DT, variable)
        max    = self.UA.get_max(DT, variable)
        nans   = self.UA.get_nan_count(DT, variable)

        statistics = [mean, median, nans, stddev, min, max]
        lineEdits  = [self.window.de_le_mean_2,
                      self.window.de_le_median_2,
                      self.window.de_le_nan_2,
                      self.window.de_le_std_2,
                      self.window.de_le_min_2,
                      self.window.de_le_max_2
                      ]
        it = 0
        for le in lineEdits:
            GUI_utils.set_lineEdit_text(le, str(statistics[it]))
            it += 1

        quartiles = self.__compute_quartiles(DT, variable)
        self.__put_quartiles_into_tw(quartiles)
        decils    = self.__compute_decils(DT, variable)
        self.__put_decils_into_tw(decils)

        current_plot = self.window.de_cb_plot_selector.currentText()
        plot_widget  = self.window.de_fr_plot
        if current_plot in self.plot_types:
            self.__generate_numeric_plot(DT, variable, plot_widget, current_plot)

    def __compute_quartiles(self, DT, variable):
        quartiles = []
        for i in range(0, 3):
            quartiles.append(self.UA.get_quantile(DT, variable, q=i*0.25))
        return quartiles

    def __put_quartiles_into_tw(self, quartiles):
        quartiles2D    = []
        quartile_count = 1
        for quartile in quartiles:
            quartiles2D.append([quartile_count, quartile])
            quartile_count += 1

        headers = ("No of quartile", "Quartile's value")
        quartiles_tw = self.window.de_tw_quartiles
        GUI_utils.populate_tableWidget(quartiles_tw
                                      ,quartiles2D
                                      ,headers)

    def __compute_decils(self, DT, variable):
        decils = []
        for i in range(0, 9):
            decils.append(self.UA.get_quantile(DT, variable, q=i*0.1))
        return decils

    def __put_decils_into_tw(self, decils):
        decils2D     = []
        decile_count = 1
        for decile in decils:
            decils2D.append([decile_count, decile])
            decile_count += 1

        headers = ("No of a decile", "The decils's value")
        decils_tw = self.window.de_tw_decils
        GUI_utils.populate_tableWidget(decils_tw
                                      ,decils2D
                                      ,headers)

    def __generate_numeric_plot(self, DT, variable, widget, current_plot):
        if current_plot == 'Histogram':
          self.UA.plot_histogram(DT, variable, widget)
        elif current_plot == 'Boxplot':
          self.UA.plot_boxplot(DT, variable, widget)
        else: #Values' plot
          self.UA.plot_values(DT, variable, widget)

    def __character_exploration(self, DT, variable):
        unique_counts = self.UA.get_uniq_vars_count(DT, variable)
        frequencies    = self.UA.get_frequencies(DT, variable)

        uniqs_count_le = self.window.de_le_uniqs
        GUI_utils.set_lineEdit_text(uniqs_count_le
                                   ,str(unique_counts))
        self.__put_freqs_into_tw(frequencies)

        self.UA.plot_barplot(DT, variable, self.window.de_fr_bar)
        self.UA.plot_piechart(DT, variable, self.window.de_fr_pie)

    def __put_freqs_into_tw(self, frequencies):
        frequencies2D =[]
        for key_val in frequencies.keys():
            frequencies2D.append([key_val, str(frequencies[key_val])])

        freq_tw = self.window.de_tw_freqs
        headers = ('Value', "Value's frequency")

        GUI_utils.populate_tableWidget(freq_tw, frequencies2D, headers)
