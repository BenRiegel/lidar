##------------------------------------------------------------------------------
## Name: vlr.py
##
## Description: contains the VLRBlock class and the VLR class. The former
## represents the variable length records in the las file. The latter
## represents each individual record
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#-----imports ------------------------------------------------------------------

from unit import Unit
from section import Section


#----- public api --------------------------------------------------------------

class VLR(Section):
    def __init__(self, num):
        super().__init__()
        self.name = f'VLR {num}'

class VLRBlock:
    def __init__(self):
        self.name = 'Variable Length Records'
        self.offset = None
        self.records = []
        self.size = Unit(0)

    def get_record(self, num):
        return self.records[num]
