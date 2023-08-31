class DataTable:
    """
Its a wrapper-class for a pandas DataFrame. It of course keeps the df itself
but also have additional informative attributes available to get using getter methods.
It also offers a short summary string / print via get_summary() method.
DataTable can pickle-save itself using the save() method.
    """
    def __init__(self, pddf, name=''):
        """
Creates an DataTable object with its informative attributes filled.
The attributes' values are infered based on the input Pandas DataFrame.
----------
Parameters:
pddf    - a pandas dataframe which needs the wrapping
name () - a metadata name to be given to the wrapped DataFrame
        """
        import pandas as pd
        self.__data = pddf
        self.__types = self.__data.dtypes.to_dict()
        self.__variables = list(self.__types.keys())
        self.__shape = self.__data.shape
        self.__name = name
        
    def get_core(self):
        """
A basic getter method. It returns the DataFramed stored in DataTable
        """
        return self.__data
    
    def get_name(self):
        """
A basic getter method. It returns the name of the DataTable        
        """
        return self.__name
    
    def get_types(self):
        """
A basic getter method. It returns a dictionary of the DataFrame variables-types        
        """
        return self.__types
    
    def get_variables(self):
        """
A basic getter method. It returns names of the DataTable's variables        
        """
        return self.__variables
    
    def get_shape(self):
        """
A basic getter method. It returns a shape of the DataFrame (rows and cols counts)
        """
        return self.__shape
    
    def get_summary(self):
        """
A verbose method. It returns the string containing info about the stored DataFrame.
It includes: example data, name of the DataTable, available columns and their types
        """
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
    
    def save(self, interactive=True, dir_path='', force=False):
        """
This method dumps a DataTable into a pickle (.pkl) file.
----------
Parameters:
interactive - True|False. If true make a dialogue to ask for a destination directory
dir_path    - A path to a directory where we want to save a pkl. If '' its gonna be pwd
force       - True|False if True we overwrite the pickle if it already exists.
        """
        if interactive not in (True, False):
            raise ValueError('interactive parameter can be only True/False') 
        if force not in (True, False):
            raise ValueError('force parameter can be only True/False')
        if interactive == True:
            import easygui
            dir_path = easygui.diropenbox()
            
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

    def sort(self, sort_dict):
        df = self.get_core()
        return df.sort_values(
            by=list(sort_dict.keys())
            ,ascending=list(sort_dict.values())
        )