##------------------------------------------------------------------------------
## Name: data_types.py
##
## Description: contains a method retrieving the classification codes for a
## given point format
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#----- imports -----------------------------------------------------------------

from utils import get_csv_lines


#----- private code block ------------------------------------------------------

def get_codes(version):
    schema_file = f'../Schema/Classifications_{version}.csv'
    lines = get_csv_lines(schema_file)
    return lines


#----- public api --------------------------------------------------------------

def get_class_codes(point_format):
    if point_format in range(0, 6):
        return get_codes('A')
    else:
        return get_codes('B')
