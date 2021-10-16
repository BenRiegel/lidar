##------------------------------------------------------------------------------
## Name: section_ctrl.py
##
## Description: contains functions for manipulating instances of the Section
## class
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#-----imports ------------------------------------------------------------------

from utils import get_csv_lines
from format import Format
from datum import Datum


#----- private code block ------------------------------------------------------

def parse_csv_lines(section, lines):
    offset = section.offset
    for line in lines:
        key = line[0]
        name = line[1]
        format_str = line[2]
        format = Format(format_str)
        datum = Datum(name, offset, format)
        section.add_datum(key, datum)
        section.increment_size(datum.size)
        offset += datum.size


#----- public api --------------------------------------------------------------

def get_schema(csv_file):
    lines = get_csv_lines(csv_file)
    return lines

def load_schema(section, csv_file):
    lines = get_csv_lines(csv_file)
    parse_csv_lines(section, lines)

def read_values(section, las_file):
    for datum in section.data.values():
        value = las_file.read_datum(datum.offset, datum.format)
        datum.value = value

def write_values(section, las_file):
    for datum in section.data.values():
        las_file.write_datum(datum.offset, datum.format, datum.value)
