##------------------------------------------------------------------------------
## Name: unpack.py
##
## Description: contains functions for retrieving pack/unpack codes for later
## use in struct.pack/unpack functions
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#----- private code block ------------------------------------------------------

TYPE_CODES = {
    'bit'                : 'B',
    'char'               : 'b',
    'unsigned char'      : 'B',
    'text'               : 'c',
    'short'              : 'h',
    'unsigned short'     : 'H',
    'long'               : 'l',
    'unsigned long'      : 'L',
    'long long'          : 'q',
    'unsigned long long' : 'Q',
    'double'             : 'd',
}


#----- public api --------------------------------------------------------------

LITTLE_ENDIAN_CODE = '<'
BIG_ENDIAN_CODE = '>'

def calc_unpack_code(data_type, num_values, offset):
    type_code = TYPE_CODES[data_type]
    unpack_code = type_code * num_values
    return unpack_code

def calc_pack_code(data_type, num_values):
    type_code = TYPE_CODES[data_type]
    pack_code = type_code * num_values
    return pack_code
