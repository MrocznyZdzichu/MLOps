from abc import ABC, abstractmethod

class GenericLoader(ABC):
    def __init__(self):
        pass

    def get_possible_parameters(self):
        msg      = self._msg
        params   = self._params
        defaults = self._defaults
        types    = self._types
        return msg, params, defaults, types
    
    @abstractmethod
    def load_to_df(self, path, import_params={}):
        pass

    @abstractmethod
    def load_to_DT(self, path, import_params={}, filename=''):
        pass