import pandas as pd

from GenericLoader import GenericLoader


class DL_csvLoader(GenericLoader):
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

    def get_possible_parameters(self):
        return super().get_possible_parameters()