class DataRepository:
    def __init__(self, deployment_dir='', interactive=True):
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
        selfstore_file = self.__deployment_dir + '\\' + self.__reserved_for_this + '.pkl'
        
        if not os.path.isfile(selfstore_file):
            self.__maintained_DTs = []
            self.__feature_store  = {}
            self.__DTs_variables  = {}    
            self.__DTs_shapes     = {}
            self.__DTs_summaries  = {}
        
        else:
            self.__restore_self(selfstore_file)
        
    def __restore_self(self, dump_loc):
        import pickle
        with open(dump_loc, 'rb') as dump:
            saved_state = pickle.load(dump)
            
        self.__maintained_DTs = saved_state.get_maintained_DTs()
        self.__feature_store  = saved_state.get_feature_store()
        self.__DTs_variables  = saved_state.get_variables()
        self.__DTs_shapes     = saved_state.get_shapes()
        self.__DTs_summaries  = saved_state.get_summaries()
        
        
    def add_DataTable(self, DT):
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
        
        self.__store_DT_pickle(DT)
        
    def __store_DT_pickle(self, DT):
        pickle_loc = self.__deployment_dir
        DT.save(interactive=False, dir_path=pickle_loc)
        
    def remove_DataTable(self, DT_name):
        if not isinstance(DT_name, str):
            raise TypeError(f'A DataTable name must be a string. Passed a {type(DT_name)} instead.')
        if DT_name not in self.__maintained_DTs:
            raise ValueError(f'DataTable object named {DT_name} is not maintained in the repository.')
            
        import os
        setup_dicts = (self.__feature_store
                       ,self.__DTs_variables
                       ,self.__DTs_shapes
                       ,self.__DTs_summaries
        )
        for store in setup_dicts:
            del store[DT_name]
            
        self.__maintained_DTs.remove(DT_name)
        physical_storage_loc = self.__deployment_dir + '\\' + DT_name + '.pkl' 
        if not os.path.isfile(physical_storage_loc):
            raise ValueError("The DataTable's pickle is missing. Critical error!")
            
        os.remove(physical_storage_loc)
        
        self.save()
        
    def save(self):
        import pickle
        save_store = self.__deployment_dir + '\\' + self.__reserved_for_this + '.pkl'
        with open(save_store, 'wb') as store:
            pickle.dump(self, store)
            
    def drop_repo(self):
        for stored_data in self.__maintained_DTs:
            self.remove_DataTable(stored_data)
        
        import os
        selfstorage_path = self.__deployment_dir + '\\' + self.__reserved_for_this + '.pkl'
        os.remove(selfstorage_path)
        
        self = self.__init__(self.__deployment_dir, interactive=0)
        
    def get_deployment_dir(self):
        return self.__deployment_dir
    
    def get_maintained_DTs(self):
        return self.__maintained_DTs
    
    def get_feature_store(self, DT_name=''):
        return self.__dict_getter_core(self.__feature_store, DT_name=DT_name)
            
    def get_variables(self, DT_name=''):
        return self.__dict_getter_core(self.__DTs_variables, DT_name=DT_name)
    
    def get_shapes(self, DT_name=''):
        return self.__dict_getter_core(self.__DTs_shapes, DT_name=DT_name)
    
    def get_summaries(self, DT_name=''):
        return self.__dict_getter_core(self.__DTs_summaries, DT_name=DT_name)
    
    def __dict_getter_core(self, attribute, DT_name=''):
        if not isinstance(DT_name, str):
            raise TypeError('Provided saved DataTable name ought to be a string')
        
        if DT_name == '':
            return attribute
        elif DT_name not in self.get_maintained_DTs():
            raise ValueError('The name you provided doesnt name an existing DataTable in the Repository')
        else:
            return attribute[DT_name]
