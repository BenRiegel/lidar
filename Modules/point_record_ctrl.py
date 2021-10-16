##------------------------------------------------------------------------------
## Name: point_record_ctrl.py
##
## Description: contains methods performed on instances of the PointRecord
## class, including the method of cycling through the points in an las file
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#-----imports ------------------------------------------------------------------

from section_ctrl import load_schema, get_schema
from header_ctrl import update_header, reset_header
from unit import Unit
from utils import EmptyClass


#---- private code block -------------------------------------------------------

def get_csv_file(num):
    schema_file = f'../Schema/Point_Format_{num}.csv'
    return schema_file

def load_decoder(las_file, point_record):
    las_file.decoder.reset()
    for datum in point_record.data.values():
        format = datum.format
        las_file.decoder.add_record(format)

def convert_raw_data(point_record, raw_data, header):
    public_point_record = EmptyClass()
    i = 0
    for key, value in point_record.data.items():
        value = raw_data[i]
        setattr(public_point_record, key, value)
        i+=1
    public_point_record.x *= header.get_datum('x_scale').value + header.get_datum('x_offset').value
    public_point_record.y *= header.get_datum('y_scale').value + header.get_datum('y_offset').value
    public_point_record.z *= header.get_datum('z_scale').value + header.get_datum('z_offset').value
    return public_point_record


#----- public api --------------------------------------------------------------

def get_point_schema(num):
    csv_file = get_csv_file(num)
    schema = get_schema(csv_file)
    return schema

def load_point_record(point_record, offset_point_data, num):
    point_record.offset = Unit(offset_point_data)
    csv_file = get_csv_file(num)
    load_schema(point_record, csv_file)

def cycle_points(las_file, metadata, out_las, out_metadata, funct):
    reset_header(out_metadata.header)
    load_decoder(las_file, metadata.point_record)
    block_size = las_file.decoder.get_block_size()
    num_points = metadata.header.get_datum('num_points').value
    num_points = 10000
    offset_point_data = metadata.header.get_datum('offset_point_data').value
    las_file.set_offset(offset_point_data)
    for i in range(0, num_points):
        bytes = las_file.read_bytes(block_size)
        raw_data = las_file.decoder.decode_bytes(bytes)
        point_data = convert_raw_data(metadata.point_record, raw_data, metadata.header)
        keep = funct(point_data)
        if keep:
            update_header(out_metadata.header, point_data)
            out_las.write_bytes(bytes)
