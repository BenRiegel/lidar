##------------------------------------------------------------------------------
## Name: metadata.py
##
## Description: contains method for loading metadata from las file
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#-----imports ------------------------------------------------------------------

from las import LASFile
from header import Header
from las_ctrl import verify_las, get_version
from utils import EmptyClass, get_csv_lines
from header_ctrl import load_header
from global_encoding_ctrl import load_global_encoding
from vlr_ctrl import load_vlr_block
from point_record_ctrl import load_point_record


#----- private code block ------------------------------------------------------

SUPPORTED_VERSIONS = ['1.0', '1.1', '1.2', '1.3', '1.4']

SECTIONS_INFO_FILE = '../Schema/File_Sections_Info.csv'

def verify_version(version):
    if not version in SUPPORTED_VERSIONS:
        print(version + ' is not a supported LAS file format')

def parse_csv_lines(lines):
    version_info = {}
    for line in lines:
        key = line[0]
        info = EmptyClass()
        info.has_global_encoding = True if line[1] == 'Y' else False
        info.vlr_format = line[2]
        info.has_data_sig = True if line[3] == 'Y' else False
        info.has_evlr = True if line[4] == 'Y' else False
        version_info[key] = info
    return version_info

def get_sections_info(version):
    lines = get_csv_lines(SECTIONS_INFO_FILE)
    info = parse_csv_lines(lines)
    version_info = info[version]
    return version_info

def init_metadata(las_file, metadata):
    verify_las(las_file)
    version = get_version(las_file)
    verify_version(version)
    load_header(metadata.header, las_file, version)
    sections_info = get_sections_info(version)
    if sections_info.has_global_encoding:
        global_encoding_parent = metadata.header.get_datum('global_encoding')
        load_global_encoding(metadata.global_encoding, global_encoding_parent, version)
    load_vlr_block(metadata.vlr_block, sections_info.vlr_format, metadata.header, las_file)
    point_record_fmt = metadata.header.get_datum_value('point_record_fmt')
    offset_point_data = metadata.header.get_datum_value('offset_point_data')
    load_point_record(metadata.point_record, offset_point_data, point_record_fmt)


#----- public api --------------------------------------------------------------

def load_metadata(metadata, las_file):
    las_file.open_and_do('read', init_metadata, metadata)
