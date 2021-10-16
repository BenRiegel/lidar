##------------------------------------------------------------------------------
## Name: lidar.py
##
## Description: LidarDataset class that can be used to print metadata and to
##   filter points to a new las dataset
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#----- imports -----------------------------------------------------------------

from las import LASFile
from metadata import Metadata
from metadata_ctrl import load_metadata
from las_ctrl import filter_points
from vlr_ctrl import read_vlr_payload
from classifications_ctrl import get_class_codes
from point_record_ctrl import get_point_schema
import view_ctrl


#----- public api --------------------------------------------------------------

class LidarDataset:
    def __init__(self, file):
        self.file = file
        self.las_file = LASFile(file)
        self.metadata = Metadata()
        load_metadata(self.metadata, self.las_file)

    def filter_points(self, funct, out_file):
        filter_points(self.las_file, self.metadata, funct, out_file)

    def print_header(self):
        header = self.metadata.get_header()
        view_ctrl.print_header(self.file, header)

    def print_global_encoding(self):
        global_encoding = self.metadata.get_global_encoding()
        view_ctrl.print_global_encoding(self.file, global_encoding)

    def print_vlrs(self):
        vlrs = self.metadata.get_vlrs()
        view_ctrl.print_vlr_block(self.file, vlrs)

    def print_vlr_payload(self, num):
        vlr = self.metadata.get_vlr(num)
        payload = read_vlr_payload(vlr, self.las_file)
        view_ctrl.print_vlr_payload(self.file, num, payload)

    def print_point_format(self):
        point_format = self.metadata.get_point_format()
        schema = get_point_schema(point_format)
        view_ctrl.print_point_format(self.file, point_format, schema)

    def print_classification_codes(self):
        point_format = self.metadata.get_point_format()
        class_codes = get_class_codes(point_format)
        view_ctrl.print_class_codes(self.file, point_format, class_codes)
