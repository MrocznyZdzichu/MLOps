class DataRepository:
    """
A class implementing a repostory of the pre-loaded data. It enables to:
* store the date in a persistent way and retrieve them easily
* gain an easy access to metadata such as dtypes or register times
* provide an easy way to delete data which is not needed anymore
The class is implements standard in-code interface but it offers an interactive mode also.

Repository stores itself in pickle files in the deployment directory.
A Resoritory's state is every modification.
    """
    def __init__(self, deployment_dir='', interactive=True):
        """
A constructor which creates a blank, new repository or restores actually physical-existant one.
-----------
Parameters:
* deployment_dir - if interactive is False then it has to be passed.
                   its a path to the deployment_dir which will keep repo's and data's pickles
* interactive    - True or False. If True you do not need to provide the deployment_dir parameter.
                   A window shall appear which will prompt the user for the path.
                   
The constructor doesnt create the repo's pickle - it will be created after 1st data loading.
If the repo is brand new its metadata will be initialised by empty lists/dictionaries.
        """
        if interactive not in (True, False):
            raise ValueError('The interactivity mode must be True or False.')
            
        import os
        if interactive == False:
            if os.path.isdir(deployment_dir):
                self.__deployment_dir = deployment_dir
            else:
                raise ValueError('Provided path doesnt point to an existing directory.')
                
        else:
            import easygui
            self.__deployment_dir = easygui.diropenbox()
            
        self.__reserved_for_this = 'DATAREPOSITORY_SELFSTORAGE'
        selfstore_file = self.__get_DT_site(self.__reserved_for_this)
        
        if not os.path.isfile(selfstore_file):
            self.__maintained_DTs    = []
            self.__feature_store     = {}
            self.__DTs_variables     = {}    
            self.__DTs_shapes        = {}
            self.__DTs_summaries     = {}
            self.__DTs_register_time = {}
        
        else:
            self.__restore_self(selfstore_file)
        
    def __restore_self(self, dump_loc):
        import pickle
        with open(dump_loc, 'rb') as dump:
            saved_state = pickle.load(dump)
            
        self.__maintained_DTs    = saved_state.get_maintained_DTs()
        self.__feature_store     = saved_state.get_feature_store()
        self.__DTs_variables     = saved_state.get_variables()
        self.__DTs_shapes        = saved_state.get_shapes()
        self.__DTs_summaries     = saved_state.get_summaries()
        self.__DTs_register_time = saved_state.get_register_times()
        
    def add_DataTable(self, DT):
        """
A method implementing registering a DataTable object into the repository:
-----------
Parameters:
DT - A data table object which you want to register into the self repository
        """
        import DataTable
        if not isinstance(DT, DataTable.DataTable):
            raise TypeError('Provided input is not a DataTable object.')
            
        added_DT_name = DT.get_name()
        if added_DT_name in self.__maintained_DTs:
            raise ValueError('Provided DataTable is already kept in our repository.')
        if added_DT_name == self.__reserved_for_this:
            raise ValueError(f'{added_DT_name} is reserved for the repository selfstorage.')
            
        self.__register_DT(DT, added_DT_name)
        self.save()
    
    def __register_DT(self, DT, name):
        self.__maintained_DTs.append(name)
        self.__feature_store[name] = DT.get_types()
        self.__DTs_variables[name] = DT.get_variables()
        self.__DTs_shapes[name]    = DT.get_shape()
        self.__DTs_summaries[name] = DT.get_summary()
        
        from numpy import datetime64
        self.__DTs_register_time[name]   = datetime64('now')
        self.__store_DT_pickle(DT)
        
    def __store_DT_pickle(self, DT):
        pickle_loc = self.__deployment_dir
        DT.save(interactive=False, dir_path=pickle_loc)
        
    def remove_DataTable(self, DT_name):
        """
A method implementing deleting a DataTable object from the self repository.
The method will remove DT's metadata and the pickle both.
A ValueError will be raised when passed DT_name is not indicating a registered DT. 
-----------
Parameters:
DT_name - a name of the DataTable which we wish to remove. 
        """
        if not isinstance(DT_name, str):
            raise TypeError(f'A DataTable name must be a string. Passed a {type(DT_name)} instead.')
        if DT_name not in self.__maintained_DTs:
            raise ValueError(f'DataTable object named {DT_name} is not maintained in the repository.')
            
        import os
        setup_dicts = (self.__feature_store
                       ,self.__DTs_variables
                       ,self.__DTs_shapes
                       ,self.__DTs_summaries
                       ,self.__DTs_register_time
        )
        for store in setup_dicts:
            del store[DT_name]
            
        self.__maintained_DTs.remove(DT_name)
        physical_storage_loc = self.__get_DT_site(DT_name)

        if not os.path.isfile(physical_storage_loc):
            raise RuntimeError("The DataTable's pickle is missing. Critical error!")
            
        os.remove(physical_storage_loc)
        
        self.save()
        
    def save(self):
        """
A method implemeting saving the repository's state.
Its an easy oneliner: call and a pickle is made.
        """
        import pickle
        save_store = self.__get_DT_site(self.__reserved_for_this)
        with open(save_store, 'wb') as store:
            pickle.dump(self, store)
            
    def drop_repo(self):
        """
A method implemeting deleting a repository AND ALL STORED DATATABLES.
It deletes physically all the pickles from the deployment_dir
        """
        from copy import copy
        DTs = copy(self.__maintained_DTs)

        for stored_data in DTs:
            self.remove_DataTable(stored_data)
        
        import os
        
        selfstorage_path = self.__get_DT_site(self.__reserved_for_this)
        if os.path.isfile(selfstorage_path):
            os.remove(selfstorage_path)
        
    def get_deployment_dir(self):
        """
Returns a deployment_dir path of self        
        """
        return self.__deployment_dir
    
    def get_DT(self, DT_name):
        """
DataTable object getter. It is an interface to gather the data from the repository.
-----------
Parameters:
DT_name - a name of the DataTable you wish to get.
-----------
Returns:
A DataTable object (not the pandas.DataFrame only)
-----------:
TypeError    - if the DT_name is not a string
ValueError   - if the DT_name doesnt point to an already registered DataTable
RuntimeError - if the data is registered but there is not pickle storing it. Some fckup anyway.
        """
        if not isinstance(DT_name, str):
            raise TypeError("A DataTable's name must be a string.")
        if DT_name not in self.__maintained_DTs:
            raise ValueError("There is not a such DataTable as passed.")
        
        DT_pickle_loc = self.__get_DT_site(DT_name)
        
        import os
        if not os.path.isfile(DT_pickle_loc):
            raise RuntimeError('Data not found but it was registered. Recreating the repository is adviced')
            
        import pickle
        with open(DT_pickle_loc, 'rb') as site:
            return pickle.load(site)
        
    def get_maintained_DTs(self):
        """
A getter method for the a list of the registered DataTables' names.        
        """
        return self.__maintained_DTs
    
    def get_feature_store(self, DT_name=''):
        """
A getter method for a dictionary containing informations about dtypes of DataTables stored in self.
-----------
Parameters:
DT_name - if you pass it you will get the dtypes info only about the given DT
-----------
Returns:
A dictionary DT_name : dtypes with info about registered DataTables
If DT_name is passed only one dtypes is returned instead of the full dictionary
        """
        return self.__dict_getter_core(self.__feature_store, DT_name=DT_name)
            
    def get_variables(self, DT_name=''):
        """
A getter method for a dictionary containing informations about columns of DataTables stored in self.
-----------
Parameters:
DT_name - if you pass it you will get the columns info only about the given DT
-----------
Returns:
A dictionary DT_name : columns with info about registered DataTables
If DT_name is passed only one columns info is returned instead of the full dictionary
        """
        return self.__dict_getter_core(self.__DTs_variables, DT_name=DT_name)
    
    def get_shapes(self, DT_name=''):
        """
A getter method for a dictionary containing informations about shapes of DataTables stored in self.
-----------
Parameters:
DT_name - if you pass it you will get the shapes info only about the given DT
-----------
Returns:
A dictionary DT_name : shapes with info about registered DataTables
If DT_name is passed only one shapes info is returned instead of the full dictionary
        """
        return self.__dict_getter_core(self.__DTs_shapes, DT_name=DT_name)
    
    def get_summaries(self, DT_name=''):
        """
A getter method for a dictionary containing summaries of DataTables stored in self.
-----------
Parameters:
DT_name - if you pass it you will get the summary of only the given DT
-----------
Returns:
A dictionary DT_name : summary with info about registered DataTables
If DT_name is passed only one summary is returned instead of the full dictionary
        """
        return self.__dict_getter_core(self.__DTs_summaries, DT_name=DT_name)
    
    def get_register_times(self, DT_name=''):
        """
A getter method for a dictionary containing informations about registration times of DataTables stored in self.
-----------
Parameters:
DT_name - if you pass it ypu will get the register time info only about the given DT
-----------
Returns:
A dictionary DT_name : datetime with info about registered DataTables
If DT_name is passed only one datetime info is returned instead of the full dictionary
        """
        return self.__dict_getter_core(self.__DTs_register_time, DT_name=DT_name)
    
    def __dict_getter_core(self, attribute, DT_name=''):
        if not isinstance(DT_name, str):
            raise TypeError('Provided saved DataTable name ought to be a string')
        
        if DT_name == '':
            return attribute
        elif DT_name not in self.get_maintained_DTs():
            raise ValueError('The name you provided doesnt name an existing DataTable in the Repository')
        else:
            return attribute[DT_name]
        
    def __get_DT_site(self, DT_name):
        DT_site = self.__deployment_dir + "\\" + DT_name + '.pkl'
        return DT_site
