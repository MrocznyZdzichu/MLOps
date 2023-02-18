class DataTable:
    def __init__(self, pddf, name=''):
        import pandas as pd
        self.__data = pddf
        self.__types = self.__data.dtypes.to_dict()
        self.__variables = list(self.__types.keys())
        self.__shape = self.__data.shape
        self.__name = name
        
    def get_core(self):
        return self.__data
    
    def get_name(self):
        return self.__name
    
    def get_types(self):
        return self.__types
    
    def get_variables(self):
        return self.__variables
    
    def get_shape(self):
        return self._shape
    
    def get_summary(self):
        summary = f"""
DataTable summary:
Name: {self.__name}
DataFrame preview: 
{self.__data.head()}
        
Data size: {self.__shape}
Variables:
        """
        for variable in self.__variables:
            summary += f"\n{variable} as: {self.__types[variable]}"
        return summary
    
    def save(self, dir_path='', force=False):
        if force not in (True, False):
            raise ValueError('force parameter can be only True/False')
        import pickle
        if dir_path == '':
            target_path = self.__name+'.pkl'
        else:
            target_path = dir_path + '\\' + self.__name + '.pkl'
        
        if force == False:
            import os
            if os.path.exists(target_path):
                raise ValueError('The file exists already. If you intend to overwrite, set force=True')
            
        with open(target_path, 'wb') as dump:
            pickle.dump(self, dump)
