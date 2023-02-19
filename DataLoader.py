class DataLoader:
    """
    DataLoader is a class wrapping pandas' various data load techniques in one method.
    DataLoader is able to load data interactively via dialogue windows or via standard CLI parameters.
    Currently implemented data sources:
        *.csv files
    """
    def __init__(self):
        """
        An explicit constructor which sets up current loader's configuration such as supported data types.
        This config is readable via get_loader_info() method which returns summary string.
        """
        self.__valid_interactive = (True, False)
        self.__supported_extensions = ('csv')
        
        self.__csv_msg      = 'Enter the pandas.read_csv(...) arguments. Input them in Py valid syntax'
        self.__csv_params   = ['sep', 'thousands', 'quotechar', 'decimal'
                              ,'header', 'nrows'
                              ,'names', 'true_values', 'false_values', 'na_values'
                              ,'dtype']
        self.__csv_defaults = [',', '', '', ''
                               ,'', '', ''
                               ,'', '', '', ''
                              ,'']
        self.__csv_types    = ('string', 'string', 'string', 'string'
                              ,'int', 'int'
                              ,['string'], ['string'], ['string'], ['string']
                              ,'dict')
        
    def load_data(self, interactive=True, path=None, parameters={}):  
        """
        A core method of the class. As a name of 'DataLoader' suggests - it loads data.
        By default it implements an interactive mode which means a prompt dialogues windows will open:
        * 1st window asks for a file to load.
        * 2nd window asks for additional parameters to pass. Parameters are dependant on the source's type
        
        Parameters:
        * interactive (True) - The mode of loading. If True (default) we will be prompted by GUI windows.
                               Otherwise we need to explict pass the data path and the import's parameters 
        * path        = None - Used only when interactive is False. It is an explicit path to the imported file.
        * parameters  = {}   - Used only when interactive is False. This is a dictionary of keywords parameters
                               for importing the data. 
                               
        Returns:
        *  a DataTable object containing the imported data + some metadata.
        """
        if not self.__validate_interactive(interactive):
            raise ValueError('Wrong interactivity mode passed.')
            
        if interactive == True:
            import easygui
            path = easygui.fileopenbox()
            
        elif type(path) != str or len(path) == 0 or type(parameters) != dict:
             raise ValueError('Explicit parameters not specified properly')   
        
        extension = path.split('.')[-1]
        
        if self.__validate_path_extension(extension) == False:
            raise ValueError("Empty or unsupported input file's path")
            
        if interactive == True:
            msg, fieldNames, defaults, types = self.__get_possible_parameters(extension)           
            import_params = self.__open_params_window(msg, fieldNames, defaults)
            import_params = self.__process_parameters(import_params, defaults, types)
        else:
            import_params = parameters

        df = self.__pandas_loader(path, extension, import_params)
        filename = path.split('\\')[-1].split('.')[0]
                              
        from DataTable import DataTable as DT
        return DT(df, name=filename)
    
    def load_saved_DT(self, pickle_path):
        """
A method to load a DataTable instance stored in a pickle file.
It requires pickle_path (string) as a parameter - a path to the pickle.
It returns the resolved DataTable instance of course.
        """
        if pickle_path[-4:] != '.pkl':
            raise ValueError('The path must specify a pickle dump')
            
        import pickle
        import DataTable as DT
        with open(pickle_path, 'rb') as dump:
            readen = pickle.load(dump)
            if isinstance(readen, DT.DataTable):
                return readen
            else:
                raise TypeError('Readen file must be a DataTable instance')
                
    def get_loader_info(self):
        """
        A typical informative/sumamry method. It returns an info string about:
        * valid interactivity modes (that ones are quite obvious though)
        * supported extensions / data sources
        * type-specific parameters' details
        
        The info is a totally low-effort hardcode of the class atributes, but it stills acheive its verbose role.
        """
        info_string = """
        self.__valid_interactive = (True, False)
        self.__supported_extensions = ('csv')
        
        self.__csv_msg      = 'Enter the pandas.read_csv(...) arguments. Input them in Py valid syntax'
        self.__csv_params   = ['sep', 'thousands', 'quotechar', 'decimal'
                              ,'header', 'nrows'
                              ,'names', 'true_values', 'false_values', 'na_values'
                              ,'dtype']
        self.__csv_defaults = [',', '', '', ''
                               ,'', '', ''
                               ,'', '', '', ''
                              ,'']
        self.__csv_types    = ('string', 'string', 'string', 'string'
                              ,'int', 'int'
                              ,['string'], ['string'], ['string'], ['string']
        """
        return info_string
        
    def __validate_interactive(self, interactive):
        return interactive in self.__valid_interactive
    
    def __validate_path_extension(self, extension):
        return extension in self.__supported_extensions
    
    def __get_possible_parameters(self, extension):
        if extension == 'csv':
            msg      = self.__csv_msg
            params   = self.__csv_params
            defaults = self.__csv_defaults
            types    = self.__csv_types
        
        return msg, params, defaults, types
    
    def __open_params_window(self, msg, fieldNames, defaults=()):
        import easygui
        title = "Data import's details"
        parameters = easygui.multenterbox(msg, title, fieldNames, values=defaults)
        
        parameters_as_dict = {}
        dicted = 0
        for par in fieldNames:
            parameters_as_dict[par] = parameters[dicted]
            dicted += 1
        
        return parameters_as_dict
        
    def __process_parameters(self, parameters, defaults, types):
        import numpy as np
        import copy
        processed_parameters = copy.copy(parameters)
        
        it = 0
        for key in parameters:
            value = parameters[key]
            if value in ('None', ''):
                del processed_parameters[key]
                it += 1
                continue
              
            if types[it] != 'string':
                processed_parameters[key] = eval(value)
             
            it += 1
        
        return processed_parameters
            
    def __pandas_loader(self, path, extension, parameters):
        import pandas as pd
        if extension == 'csv':
            return pd.read_csv(path, **parameters)
