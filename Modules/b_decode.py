##------------------------------------------------------------------------------
## Name: b_decode.py
##
## Description: contains the Decoder class, which is used in an las file
## to convert data from a binary format to a python data type
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#-----imports ------------------------------------------------------------------

import struct
from utils import EmptyClass, trim_list
from unpack import calc_unpack_code
from unit import Unit


#----- private code block ------------------------------------------------------

def process_as_bit(list, format, offset):
    parent_value = list[0]
    parent_bits = 8
    bin_str = '1' * parent_bits
    i = int(bin_str, 2)
    bit_offset = offset.bits
    data = parent_value >> bit_offset
    num_bits = format.num_values
    mask = i >> (parent_bits - num_bits)
    result = data & mask
    return result

def process_as_text(list):
    text = ''
    for char in list:
        text += char.decode('ascii')
    return text

def process_as_num(list):
    return list[0]

def process_as_list(list):
    return list

def process_unpack_result(values, format, offset):
    if format.data_type == 'bit':
        value = process_as_bit(values, format, offset)
    elif format.data_type == 'text':
        value = process_as_text(values)
    else:
        if format.num_values == 1:
            value = process_as_num(values)
        else:
            value = process_as_list(values)
    return value


#----- public api --------------------------------------------------------------

class Decoder:
    def __init__(self, endian_code):
        self._endian_code = endian_code
        self.records = []
        self.size = Unit(0)

    def reset(self):
        self.records = []
        self.size = Unit(0)

    def add_record(self, format):
        record = EmptyClass()
        record.offset = self.size.copy()
        record.format = format
        unpack_code = calc_unpack_code(format.data_type, format.num_values, record.offset)
        record.unpack_str = self._endian_code + unpack_code
        self.records.append(record)
        self.size += format.size

    def decode_bytes(self, bytes):
        values = []
        for record in self.records:
            offset_bytes = record.offset.bytes
            unpack_result = struct.unpack_from(record.unpack_str, bytes, offset_bytes)
            value = process_unpack_result(unpack_result, record.format, record.offset)
            values.append(value)
        trimmed_list = trim_list(values)
        return trimmed_list

    def get_block_size(self):
        return self.size.bytes
