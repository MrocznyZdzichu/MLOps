import pandas as pd

from GenericLoader import GenericLoader
from DataTable import DataTable as DT
        

class CSVLoader(GenericLoader):
    def __init__(self):
        self._msg      = 'Enter the pandas.read_csv(...) arguments. Input them in Py valid syntax'
        self._params   = ['sep', 'thousands', 'quotechar', 'decimal'
                              ,'header', 'nrows'
                              ,'names', 'true_values', 'false_values', 'na_values'
                              ,'dtype']
        self._defaults = [',', '', '', ''
                               ,'', '', ''
                               ,'', '', '', ''
                              ,'']
        self._types    = ('string', 'string', 'string', 'string'
                              ,'int', 'int'
                              ,['string'], ['string'], ['string'], ['string']
                              ,'dict')

    def load_to_df(self, path, import_params={}):
        return pd.read_csv(path, **import_params)
    
    def load_to_DT(self, path, import_params={}, filename=''):
        df = self.load_to_df(path, import_params)
        if filename != '':
            return DT(df, name=filename)
        else:
            print('No filename specified, returning Pandas.DataFrame instead')
            return df

    def get_possible_parameters(self):
        return super().get_possible_parameters()