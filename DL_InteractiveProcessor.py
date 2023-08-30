import easygui
import numpy as np
import copy


class DL_InteractiveProcessor:
    def __init__(self) :
        pass

    def get_path(self):            
        return easygui.fileopenbox()
    
    def open_params_window(msg, title, fieldNames, defaults):
        title = "Data import's details"
        parameters = easygui.multenterbox(msg, title, fieldNames, values=defaults)
        
        parameters_as_dict = {}
        dicted = 0
        for par in fieldNames:
            parameters_as_dict[par] = parameters[dicted]
            dicted += 1
        
        return parameters_as_dict
    
    def process_parameters(self, parameters, defaults, types):
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