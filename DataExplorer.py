class UnivariateAnalysis:
    def get_mean(self, DT, var):
        valid_var_params(DT, var, 'numeric')
        return DT.get_core()[var].mean()

    def get_median(self, DT, var):
        valid_var_params(DT, var, 'numeric')
        return DT.get_core()[var].median()

    def get_stddev(self, DT, var):
        valid_var_params(DT, var, 'numeric')
        return DT.get_core()[var].std()

    def get_quantile(self, DT, var, q=0.25):
        valid_var_params(DT, var, 'numeric')
        return DT.get_core()[var].quantile(q)

    def get_min(self, DT, var):
        valid_var_params(DT, var, 'numeric')
        return DT.get_core()[var].min()

    def get_max(self, DT, var):
        valid_var_params(DT, var, 'numeric')
        return DT.get_core()[var].max()

    def get_uniq_vars_count(self, DT, var):
        valid_var_params(DT, var, 'character')
        return DT.get_core()[var].nunique()

    def get_frequencies(self, DT, var):
        valid_var_params(DT, var, 'character')
        return DT.get_core()[var].value_counts().to_dict()

    def get_null_count(self, DT, var):
        valid_DT_and_var(DT, var)
        return DT.get_core()[var].isnull().sum()

    def get_nan_count(self, DT, var):
        valid_var_params(DT, var, 'numeric')
        return DT.get_core()[var].isna().sum()

    def plot_histogram(self, DT, var, widget=None):
        valid_var_params(DT, var, 'numeric')

        df = DT.get_core()

        fig, ax = prepare_plot(f'Variable {var}', 'Occurences')
        ax.hist(df[var])
        format_ticks(ax, axis='x', angle=45)

        if widget!=None:
            export_plot_to_Qt(fig, widget)
        else:
            fig.show()

    def plot_boxplot(self, DT, var, widget=None):
        valid_var_params(DT, var, 'numeric')

        df = DT.get_core()

        fig, ax = prepare_plot('', f'Variable {var}')
        ax.boxplot(df[var]
                  ,boxprops={'color' : 'blue'}
                  ,flierprops=dict(marker='.', markerfacecolor='blue', markersize=2,
                                   linestyle='none', markeredgecolor='blue')
                  ,medianprops={'color' : 'red'}
                  ,whiskerprops={'color' : 'blue'}
                  ,capprops={'color' : 'blue'}
                  )

        format_ticks(ax)
        if widget!=None:
            export_plot_to_Qt(fig, widget)
        else:
            fig.show()

    def plot_values(self, DT, var, widget=None):
        valid_var_params(DT, var, 'numeric')

        df = DT.get_core()

        fig, ax =prepare_plot('', f'Variable {var}')
        ax.plot(df[var])
        format_ticks(ax)

        if widget!=None:
            export_plot_to_Qt(fig, widget)
        else:
            fig.show()

    def plot_barplot(self, DT, var, widget=None):
        valid_var_params(DT, var, 'character')

        df = DT.get_core()

        freq = df[var].value_counts()
        if len(freq) > 7:
            freq = freq.nlargest(7)
            freq['Others'] = df[var].count() - freq.sum()

        fig, ax = prepare_plot(f"{var}'s value", 'Frequency')
        ax.bar(freq.index, freq.values)
        format_ticks(ax, axis='x', angle=45, decimal=False)

        if widget!=None:
            export_plot_to_Qt(fig, widget)
        else:
            fig.show()

    def plot_piechart(self, DT, var, widget=None):
        valid_var_params(DT, var, 'character')

        df = DT.get_core()

        freq = df[var].value_counts()
        if len(freq) > 7:
            freq = freq.nlargest(7)
            freq['Others'] = df[var].count() - freq.sum()

        fig, ax = prepare_plot('', '')
        ax.pie(freq.values, labels=freq.index, autopct='%1.1f%%', textprops={'color' : 'white'})
        if widget!=None:
            export_plot_to_Qt(fig, widget)
        else:
            fig.show()

class BivariateAnalysis:
    def get_correlation(self, DT, x, y, method='pearson'):
        x_type = get_var_type(DT, x)
        y_type = get_var_type(DT, y)

        if x_type != 'A numeric variable' or y_type != 'A numeric variable':
            raise ValueError('Both columns have to be numeric')

        return DT.get_core()[[x, y]].corr(method=method).values[0][1]

    def plot_scatterplot(self, DT, x, y, widget=None):
        valid_var_params(DT, y, 'numeric')
        valid_var_params(DT, x, 'numeric')
        df = DT.get_core()

        fig, ax = prepare_plot(f'Variable {x}', f'Variable {y}')
        ax.scatter(df[x], df[y])

        format_ticks(ax)
        if widget!=None:
            export_plot_to_Qt(fig, widget)
        else:
            fig.show()

    def get_crosscorrelation(self, DT, x, y, norm=False):
        import numpy as np

        df = DT.get_core()
        cross_corr = np.correlate(df[x], df[y], mode='same')
        if norm == True:
            cross_corr = cross_corr / np.max(cross_corr)

        max_shift = len(cross_corr) // 2
        shifts = np.arange(-max_shift, max_shift+1)

        return shifts, cross_corr

    def plot_crosscorrelation(self, DT, x, y, norm=False, widget=None):
        valid_var_params(DT, y, 'numeric')
        valid_var_params(DT, x, 'numeric')

        shifts, cross_corr = self.get_crosscorrelation(DT, x, y, norm)

        fig, ax = prepare_plot(f'Timeshifts [sample]', 'Cross-correlation')
        ax.plot(shifts, cross_corr)

#        format_ticks(ax)
        if widget!=None:
            export_plot_to_Qt(fig, widget)
        else:
            fig.show()

    def plot_corr_heatmap(self, DT, widget=None):
        import numpy as np
        import matplotlib.pyplot as plt

        df = DT.get_core()
        corr = df.corr()

        fig, ax = plt.subplots()
        heatmap = ax.pcolor(corr, cmap='coolwarm', vmin=-1, vmax=1)

        plt.xticks(np.arange(0.5, len(corr.columns), 1), corr.columns, fontsize=10, rotation=90)
        plt.yticks(np.arange(0.5, len(corr.columns), 1), corr.columns, fontsize=10)

        cbar = plt.colorbar(heatmap)

        if widget!=None:
            export_plot_to_Qt(fig, widget)
        else:
            fig.show()

def valid_var_params(DT, var, dest_type):
    valid_DT_and_var(DT, var)
    var_type = get_var_type(DT, var)
    types_dict = {
        'numeric'    : 'A numeric variable'
        ,'character' : 'A character variable'
    }

    if dest_type not in types_dict.keys():
        raise ValueError('Invalid data type specified.')

    if var_type != types_dict[dest_type]:
        raise ValueError('An action is invalid for the specified datatype.')

def get_var_type(DT, var):
    import numpy as np
    valid_DT_and_var(DT, var)

    col_type = DT.get_types()[var]

    if np.issubdtype(col_type, np.number):
        return "A numeric variable"
    elif np.issubdtype(col_type, np.datetime64):
        return "A datetime variable"
    else:
        return"A character variable"

def valid_DT_and_var(DT, var):
    import pandas as pd
    import numpy as np
    from DataTable import DataTable

    if not isinstance(DT, DataTable) or not isinstance(var, str):
        raise TypeError('Invalid types of the parameters')

    if not var in DT.get_core().columns:
        raise ValueError(f'There is not {var} column in the data')
def prepare_plot(x_desc, y_desc):
    import matplotlib.pyplot as plt
    plt.switch_backend('Qt5Agg')

    fig = plt.figure(facecolor=(20/255,30/255,40/255))
    ax = fig.add_subplot(111)
    ax.clear()
    fig.subplots_adjust(left=0.15, bottom=0.20, top=0.95, right=0.95)

    ax.set_facecolor((20/255, 30/255, 40/255))
    ax.tick_params(axis='both', which='both', colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')

    ax.set_xlabel(x_desc)
    ax.set_ylabel(y_desc)

    return fig, ax

def format_ticks(ax, axis='y', angle=45, decimal=True):
    import matplotlib.ticker as ticker

    ax.xaxis.set_major_locator(ticker.AutoLocator())
    ax.yaxis.set_major_locator(ticker.AutoLocator())
    if decimal==True:
        ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
    ax.tick_params(axis=axis, rotation=angle)

def export_plot_to_Qt(fig, widget):
    from matplotlib.figure import Figure
    from PyQt5.QtWidgets import QVBoxLayout
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

    if widget.layout() is None:
        layout = QVBoxLayout()
        widget.setLayout(layout)
    else:
        layout = widget.layout()
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

    canvas = FigureCanvas(fig)
    layout.addWidget(canvas)

    # Dodanie NavigationToolbar do layoutu
    toolbar = NavigationToolbar(canvas, widget)
    layout.addWidget(toolbar)
