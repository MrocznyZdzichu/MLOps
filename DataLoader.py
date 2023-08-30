from CSVLoader import CSVLoader
from PickleLoader import PickleLoader
from DL_InteractiveProcessor import DL_InteractiveProcessor as InteractiveProcessor


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
        self.__supported_extensions = ('csv', 'pkl')
        
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
        
        IP = InteractiveProcessor()
        if interactive == True:
            path = IP.get_path()
            
        elif type(path) != str or len(path) == 0 or type(parameters) != dict:
             raise ValueError('Explicit parameters not specified properly')   
        
        extension = path.split('.')[-1]
        
        if self.__validate_path_extension(extension) == False:
            raise ValueError("Empty or unsupported input file's path")
            
        if extension == 'csv':
            loader = CSVLoader()
        elif extension == 'pkl':
            loader = PickleLoader()

        filename = path.split('\\')[-1].split('.')[0]
        import_params = parameters

        if interactive == True:
            msg, fieldNames, defaults, types = loader.get_possible_parameters()
            if all(param != None for param in (msg, fieldNames, defaults, types)):       
                import_params = IP.open_params_window(msg, fieldNames, defaults)
                import_params = IP.process_parameters(import_params, defaults, types)

        return loader.load_to_DT(path, import_params, filename)
                              
    def load_saved_DT(self, pickle_path='', interactive=True):
        """
A method to load a DataTable instance stored in a pickle file.
----------
Parameters:
pickle_path ()     - an explicit path to the loaded pickled DataTable
interactive (True) - True for interactive mode based on easygui. False for explicit path required.
----------
Returns: 
The loaded DataTable object
        """
        if not self.__validate_interactive:
            raise ValueError('interactive flag must be one of: (True, False)')
        
        if pickle_path[-4:] != '.pkl' and interactive == False:
            raise ValueError('The path must specify a pickle dump')
    
        if interactive == True:
            import easygui
            pickle_path = easygui.fileopenbox()
        
        loader = PickleLoader()
        return loader.load_DT(pickle_path)
        
    def __validate_interactive(self, interactive):
        return interactive in self.__valid_interactive
    
    def __validate_path_extension(self, extension):
        return extension in self.__supported_extensions