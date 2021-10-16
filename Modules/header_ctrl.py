##------------------------------------------------------------------------------
## Name: header_ctrl.py
##
## Description: contains functions for manipulating instances of the Header
## class
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#-----imports ------------------------------------------------------------------

from utils import null_terminate_str, get_current_day_of_year, get_current_year
from section_ctrl import load_schema, read_values
import sys


#----- private code block ------------------------------------------------------

MAX_NUM = sys.float_info.max
MIN_NUM = -sys.float_info.max

def get_header_csv_file(version):
    version_new = version.replace('.', '_')
    schema_file = f'../Schema/Header_{version_new}.csv'
    return schema_file


#----- public api --------------------------------------------------------------

def load_header(header, las_file, version):
    csv_file = get_header_csv_file(version)
    load_schema(header, csv_file)
    read_values(header, las_file)

def reset_header(header):
    header.get_datum('num_points').value = 0
    if 'num_points_long' in header.data:
        header.get_datum('num_points_long').value = 0
    header.get_datum('num_points_by_return').value = [0]*5
    if 'num_points_by_return_long' in header.data:
        header.get_datum('num_points_by_return_long').value = [0]*15
    header.get_datum('max_x').value = MIN_NUM
    header.get_datum('max_y').value = MIN_NUM
    header.get_datum('max_z').value = MIN_NUM
    header.get_datum('min_x').value = MAX_NUM
    header.get_datum('min_y').value = MAX_NUM
    header.get_datum('min_z').value = MAX_NUM
    gen_software_str = null_terminate_str('Ben\'s LAS Updater', 32)
    header.get_datum('gen_software').value = gen_software_str
    if 'file_creation_day' in header.data:
        current_day = get_current_day_of_year()
        header.get_datum('file_creation_day').value = current_day
    if 'file_creation_year' in header.data:
        current_year = get_current_year()
        header.get_datum('file_creation_year').value = current_year

def update_header(header, point_data):
    header.get_datum('num_points').value += 1
    if 'num_points_long' in header.data:
        header.get_datum('num_points_long').value += 1
    index = point_data.return_num - 1
    point_return_counter = header.get_datum('num_points_by_return').value
    point_return_counter[index] += 1
    if 'num_points_by_return_long' in header.data:
        point_return_counter_long = header.get_datum('num_points_by_return_long').value
        point_return_counter_long[index] += 1
    if point_data.x < header.get_datum('min_x').value:
        header.get_datum('min_x').value = point_data.x
    if point_data.x > header.get_datum('max_x').value:
        header.get_datum('max_x').value = point_data.x
    if point_data.y < header.get_datum('min_y').value:
        header.get_datum('min_y').value = point_data.y
    if point_data.y > header.get_datum('max_y').value:
        header.get_datum('max_y').value = point_data.y
    if point_data.z < header.get_datum('min_z').value:
        header.get_datum('min_z').value = point_data.z
    if point_data.z > header.get_datum('max_z').value:
        header.get_datum('max_z').value = point_data.z
