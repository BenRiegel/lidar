##------------------------------------------------------------------------------
## Name: format.py
##
## Description: contains the Format class which is used to convert a shorthand
## format description from csv files (e.g. 'unsigned short [5]') into a format
## that can be used in the app
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#-----imports ------------------------------------------------------------------

from utils import EmptyClass
from data_types import get_type_size


#----- private code block ------------------------------------------------------

def parse_data_type(format_desc):
    if '[' in format_desc:
        temp = format_desc.split('[')
        data_type = temp[0]
    else:
        data_type = format_desc
    return data_type

def parse_num_values(format_desc):
    if '[' in format_desc:
        temp = format_desc.split('[')[1]
        temp2 = temp.split(']')[0]
        num_values = int(temp2)
    else:
        num_values = 1
    return num_values

def calc_size(data_type, num_values):
    type_size = get_type_size(data_type)
    size = type_size * num_values
    return size


#----- public api --------------------------------------------------------------

def Format(format_desc):
    obj = EmptyClass()
    obj.data_type = parse_data_type(format_desc)
    obj.num_values = parse_num_values(format_desc)
    obj.size = calc_size(obj.data_type, obj.num_values)
    return obj
