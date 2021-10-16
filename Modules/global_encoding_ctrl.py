##------------------------------------------------------------------------------
## Name: global_encoding_ctrl.py
##
## Description: contains functions for manipulating instances of the
## GlobalEncoding class
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#----- imports -----------------------------------------------------------------

from section_ctrl import load_schema


#----- private code block ------------------------------------------------------

def get_ge_csv_file(version):
    version_new = version.replace('.', '_')
    schema_file = f'../Schema/Global_Encoding_{version_new}.csv'
    return schema_file

def set_values(global_encoding, parent):
    for datum in global_encoding.data.values():
        parent_bits = parent.size.bytes * 8 + parent.size.bits
        bin_str = '1' * parent_bits
        i = int(bin_str, 2)
        bit_offset = datum.offset.bits
        data = parent.value >> bit_offset
        num_bits = datum.size.bits
        mask = i >> (parent_bits - num_bits)
        result = data & mask
        datum.value = result


#----- public api --------------------------------------------------------------

def load_global_encoding(global_encoding, parent, version):
    global_encoding.offset = parent.offset
    csv_file = get_ge_csv_file(version)
    load_schema(global_encoding, csv_file)
    set_values(global_encoding, parent)
