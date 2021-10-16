##------------------------------------------------------------------------------
## Name: data_types.py
##
## Description: contains a method for looking up the sizes of all the data types
## used with las files
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#-----imports ------------------------------------------------------------------

from unit import Unit


#----- private code block ------------------------------------------------------

TYPE_SIZES = {
    'bit'                : Unit(0, 1),
    'byte'               : Unit(1),
    'char'               : Unit(1),
    'unsigned char'      : Unit(1),
    'text'               : Unit(1),
    'short'              : Unit(2),
    'unsigned short'     : Unit(2),
    'long'               : Unit(4),
    'unsigned long'      : Unit(4),
    'long long'          : Unit(8),
    'unsigned long long' : Unit(8),
    'double'             : Unit(8),
}


#----- public api --------------------------------------------------------------

def get_type_size(data_type):
    type_size = TYPE_SIZES[data_type]
    return type_size
