class UnivariateAnalysis:     
    def __init__(self):
        self.num_stats_args  = {
            'quantile' : 0.5
        }
        self.num_stats_funcs = {
            'mean'      : 'df[var].mean()'
            ,'median'   : 'df[var].median()'
            ,'std'      : 'df[var].std()'
            ,'quantile' : 'df[var].quantile(self.num_stats_args["quantile"])'
            ,'min'      : 'df[var].min()'
            ,'max'      : 'df[var].max()'
        }
        self.valid_num_stats = self.num_stats_funcs.keys()
        
        self.cat_stats_funcs = {
            'uniques'      : 'df[var].nunique()'
            ,'frequencies' : 'df[var].value_counts().to_dict()'
        }
        self.valid_cat_stats = self.cat_stats_funcs.keys()

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
        
    def get_num_statistic(self, DT, var, statistic, q=None):
        if not statistic in self.valid_num_stats:
            raise ValueError(f'Statistic {statistic} is not defined in UnivariateAnalysis')
        self.__valid_var_params(DT, var, 'numeric')
    
        if statistic == 'quantile' and q != None and 0 <= q <= 1 and q != self.num_stats_args['quantile']:
            self.num_stats_args['quantile'] = q
            
        df = DT.get_core()
        return eval(self.num_stats_funcs[statistic])
    
    def get_cat_statistic(self, DT, var, statistic):
        if not statistic in self.valid_cat_stats:
            raise ValueError(f'Statistic {statistic} is not defined in UnivariateAnalysis')
        self.__valid_var_params(DT, var, 'character')
    
        df = DT.get_core()
        return eval(self.cat_stats_funcs[statistic])
    
    def plot_histogram(self, DT, var, fig_handler=None):
        self.__valid_var_params(DT, var, 'numeric')
        
        if fig_handler!= None:
            from matplotlib.figure import Figure
        import matplotlib.pyplot as plt
        
        df = DT.get_core()
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.hist(df[var])
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
            
