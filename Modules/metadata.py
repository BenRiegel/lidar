##------------------------------------------------------------------------------
## Name: metadata.py
##
## Description: contains the Metadata class, representing all the metadata
## in the las file
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#-----imports ------------------------------------------------------------------

from header import Header
from global_encoding import GlobalEncoding
from point_record import PointRecord
from vlr import VLRBlock


#----- public api --------------------------------------------------------------

class Metadata:
    def __init__(self):
        self.header = Header()
        self.global_encoding = GlobalEncoding()
        self.vlr_block = VLRBlock()
        self.point_record = PointRecord()

    def get_header(self):
        return self.header

    def get_global_encoding(self):
        return self.global_encoding

    def get_vlrs(self):
        return self.vlr_block

    def get_vlr(self, num):
        vlr = self.vlr_block.get_record(num)
        return vlr

    def get_point_format(self):
        return self.header.get_datum.value('point_record_fmt')
