import pickle
import pandas as pd
from GenericLoader import GenericLoader
from DataTable import DataTable as DT


class PickleLoader(GenericLoader):
    def __init__(self):
        self._msg      = None
        self._params   = None
        self._defaults = None
        self._types    = None

    def load_to_df(self, path, import_params={}):
        with open(path, 'rb') as f:
            input_df = pickle.load(f)
        if isinstance(input_df, pd.DataFrame) == True:
            return input_df
        else:
            raise TypeError('Pickle content is not a DataFrame as expected')
    
    def load_to_DT(self, path, import_params={}, filename=''):
        df = self.load_to_df(path, import_params)
        if filename != '':
            return DT(df, name=filename)
        else:
            print('No filename specified, returning Pandas.DataFrame instead')
            return df

    def load_DT(self, path):
        with open(path, 'rb') as file:
            input_DT = pickle.load(file)
        if isinstance(input_DT, DT) == True:
            return input_DT
        else:
            raise TypeError('Pickle content is not a DataTable object as expected')
        
    def get_possible_parameters(self):
        return super().get_possible_parameters()