class UnivariateAnalysis:     
    def get_var_type(self, DT, var):
        import numpy as np
        self.__valid_DT_and_var(DT, var)
        
        df       = DT.get_core()
        col_type = df[var].dtype
        
        if np.issubdtype(col_type, np.number):
            return "A numeric variable"
        elif np.issubdtype(col_type, np.datetime64):
            return "A datetime variable"
        else:
            return"A character variable"
        
    def get_mean(self, DT, var):
        self.__valid_var_params(DT, var, 'numeric')
        return DT[var].mean()
    
    def get_median(self, DT, var):
        self.__valid_var_params(DT, var, 'numeric')
        return DT[var].median()
    
    def get_stddev(self, DT, var):
        self.__valid_var_params(DT, var, 'numeric')
        return DT[var].std()
    
    def get_quantile(self, DT, var, q=0.25):
        self.__valid_var_params(DT, var, 'numeric')
        return DT[var].quantile(q)
    
    def get_min(self, DT, var):
        self.__valid_var_params(DT, var, 'numeric')
        return DT[var].min()
    
    def get_max(self, DT, var):
        self.__valid_var_params(DT, var, 'numeric')
        return DT[var].max()
    
    def get_uniq_vars_count(self, DT, var):
        self.__valid_var_params(DT, var, 'character')
        return df[var].nunique()
    
    def get_frequencies(self, DT, var):
        self.__valid_var_params(DT, var, 'character')
        return df[var].value_counts().to_dict()
    
    def plot_histogram(self, DT, var, widget=None):
        self.__valid_var_params(DT, var, 'numeric')

        df = DT.get_core()
        
        fig, ax = self.__prepare_plot(f'Variable {var}', 'Occurences')    
        ax.hist(df[var], color='red')
        self.__format_ticks(ax, axis='x', angle=45)
        
        if widget!=None:
            self.__export_plot_to_Qt(fig, widget)
        else:
            fig.show()
        
    def plot_boxplot(self, DT, var, widget=None):
        self.__valid_var_params(DT, var, 'numeric')

        df = DT.get_core()
        fig, ax = self.__prepare_plot('', f'Variable {var}')
        ax.boxplot(df[var]
                  ,boxprops={'color' : 'red'}
                  ,flierprops=dict(marker='.', markerfacecolor='r', markersize=2,
                                   linestyle='none', markeredgecolor='r')
                  ,medianprops={'color' : 'red'}
                  ,whiskerprops={'color' : 'red'}
                  ,capprops={'color' : 'red'}
                  )
        
        self.__format_ticks(ax)
        if widget!=None:
            self.__export_plot_to_Qt(fig, widget)
        else:
            fig.show()
            
    def __valid_DT_and_var(self, DT, var):
        import pandas as pd
        import numpy as np
        from DataTable import DataTable
        
        if not isinstance(DT, DataTable) or not isinstance(var, str):
            raise TypeError('Invalid types of the parameters')
            
        if not var in DT.get_core().columns:
            raise ValueError(f'There is not {var} column in the data')
            
    def __valid_var_params(self, DT, var, dest_type):
        self.__valid_DT_and_var(DT, var)
        var_type = self.get_var_type(DT, var)
        types_dict = {
            'numeric'    : 'A numeric variable'
            ,'character' : 'A character variable'
        }
        
        if dest_type not in types_dict.keys():
            raise ValueError('Invalid data type specified.')
        
        if var_type != types_dict[dest_type]:
            raise ValueError('An action is invalid for the specified datatype.')
            
    def __prepare_plot(self, x_desc, y_desc):
        import matplotlib.pyplot as plt
        fig = plt.figure(facecolor=(20/255,30/255,40/255))
        ax = fig.add_subplot(111)
        fig.subplots_adjust(left=0.15, bottom=0.15, top=0.85, right=0.85)
        
        ax.set_facecolor((20/255, 30/255, 40/255))
        ax.tick_params(axis='both', which='both', colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')

        ax.set_xlabel(x_desc)
        ax.set_ylabel(y_desc)
        
        return fig, ax
    
    def __format_ticks(self, ax, axis='y', angle=45):
        import matplotlib.ticker as ticker
        ax.xaxis.set_major_locator(ticker.AutoLocator())
        ax.yaxis.set_major_locator(ticker.AutoLocator())
        ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
        ax.tick_params(axis=axis, rotation=angle)
        
    def __export_plot_to_Qt(self, fig, widget):
        from matplotlib.figure import Figure
        from PyQt5.QtWidgets import QVBoxLayout
        from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
        
        canvas = FigureCanvas(fig)
        canvas.setParent(widget)
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        widget.setLayout(layout)
