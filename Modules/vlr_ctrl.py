##------------------------------------------------------------------------------
## Name: vlr_ctrl.py
##
## Description: contains methods for manipulating instances of the VLRBlock
## and VLR classes
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#----- imports -----------------------------------------------------------------

from unit import Unit
from vlr import VLR
from section_ctrl import load_schema, read_values
from utils import get_csv_lines, EmptyClass
from datum import Datum
from format import Format


#----- private clode block -----------------------------------------------------

def get_schema_file(version):
    schema_file = f'../Schema/VLR_Schema_{version}.csv'
    return schema_file

def create_record_datum(record_size, offset):
    format_desc = f'byte[{record_size}]'
    format = Format(format_desc)
    name = 'Record'
    datum = Datum(name, offset, format)
    datum.value = '[not printed]'
    return datum

def load_vlr(vlr, vlr_format, las_file):
    csv_file = get_schema_file(vlr_format)
    load_schema(vlr, csv_file)
    read_values(vlr, las_file)
    record_size = vlr.get_datum_value('record_len')
    record_offset = vlr.offset + vlr.size
    record_datum = create_record_datum(record_size, record_offset)
    record_key = 'record'
    vlr.add_datum(record_key, record_datum)
    vlr.increment_size(record_datum.size)


#----- public api --------------------------------------------------------------

def load_vlr_block(vlr_block, vlr_format, header, las_file):
    header_size = header.get_datum_value('header_size')
    num_vlrs = header.get_datum_value('num_vlrs')
    vlr_block.offset = Unit(header_size)
    offset = vlr_block.offset.copy()
    for i in range(0, num_vlrs):
        vlr = VLR(i)
        vlr.offset = offset.copy()
        load_vlr(vlr, vlr_format, las_file)
        vlr_block.records.append(vlr)
        vlr_block.size += vlr.size
        offset += vlr.size

def read_vlr_payload(vlr, las_file):
    las_file.open('read')
    record = vlr.get_datum('record')
    format_desc = f'text[{record.size.bytes}]'
    format = Format(format_desc)
    value = las_file.read_datum(record.offset, format)
    las_file.close()
    return value
