##------------------------------------------------------------------------------
## Name: las_ctrl.py
##
## Description: contains functions for manipulating instances of the LASFile
## class
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#----- imports -----------------------------------------------------------------

from las import LASFile
from format import Format
from unit import Unit
from copy import deepcopy
from point_record_ctrl import cycle_points
from section_ctrl import write_values


#----- private code block ------------------------------------------------------

FILE_SIG_OFFSET = Unit(0)
FILE_SIG_FORMAT = Format('text[4]')
REQUIRED_FILE_SIG_VALUE = 'LASF'
VER_MAJ_OFFSET = Unit(24)
VER_MIN_OFFSET = Unit(25)
VER_MAJ_MIN_FORMAT = Format('unsigned char')

def get_file_sig(las_file):
    file_sig = las_file.read_datum(FILE_SIG_OFFSET, FILE_SIG_FORMAT)
    return file_sig

def verify_file_sig(file_sig):
    if file_sig != REQUIRED_FILE_SIG_VALUE:
        print(file_sig + ' is not a valid LAS file')  #this doesn't work

def copy_to_point_data(las_file, header, out_las):
    offset_point_data = header.get_datum('offset_point_data').value
    data = las_file.read_bytes(offset_point_data)
    out_las.write_bytes(data)

def copy_to_eof(las_file, header, out_las):
    file_size = las_file.get_file_size()
    offset_point_data = header.get_datum('offset_point_data').value
    point_record_len = header.get_datum('point_record_len').value
    num_points = header.get_datum('num_points').value
    offset = offset_point_data + point_record_len * num_points
    remaining_bytes = file_size - offset
    if remaining_bytes > 0:
        las_file.set_offset(offset)
        data = las_file.read_bytes(remaining_bytes)
        out_las.write_bytes(data)


#----- public api --------------------------------------------------------------

def verify_las(las_file):
    file_sig = get_file_sig(las_file)
    verify_file_sig(file_sig)

def get_version(las_file):
    ver_maj = las_file.read_datum(VER_MAJ_OFFSET, VER_MAJ_MIN_FORMAT)
    ver_min = las_file.read_datum(VER_MIN_OFFSET, VER_MAJ_MIN_FORMAT)
    version = str(ver_maj) + '.' + str(ver_min)
    return version

def filter_points(las_file, metadata, funct, out_file):
    out_las = LASFile(out_file)
    out_metadata = deepcopy(metadata)
    out_las.open('write')
    las_file.open('read')
    copy_to_point_data(las_file, metadata.header, out_las)
    cycle_points(las_file, metadata, out_las, out_metadata, funct)
    copy_to_eof(las_file, metadata.header, out_las)
    write_values(out_metadata.header, out_las)
    las_file.close()
    out_las.close()
