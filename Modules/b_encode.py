##------------------------------------------------------------------------------
## Name: b_encode.py
##
## Description: contains the Encoder class, which is used in an las file
## to convert data from a python data type to binary data, which can then
## be written to a binary file
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#-----imports ------------------------------------------------------------------

import struct
from unpack import calc_pack_code


#----- private clode block -----------------------------------------------------

def format_as_text(value):
    byte_list = []
    for char in value:
        byte = bytes(char, 'utf-8')
        byte_list.append(byte)
    return byte_list

def format_as_list(value):
    return value

def format_as_num(value):
    return [value]

def format_value(data_type, num_values, value):
    if data_type == 'text':
        return format_as_text(value)
    else:
        if num_values == 1:
            return format_as_num(value)
        else:
            return format_as_list(value)

#----- public api --------------------------------------------------------------

class Encoder:
    def __init__(self, endian_code):
        self._endian_code = endian_code

    def encode_value(self, value, format):
        pack_code = calc_pack_code(format.data_type, format.num_values)
        pack_str = self._endian_code + pack_code
        formatted_value = format_value(format.data_type, format.num_values, value)
        bytes = struct.pack(pack_str, *formatted_value)
        return bytes
