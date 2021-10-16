##------------------------------------------------------------------------------
## Name: datum.py
##
## Description: contains the Datum class represents one data element in the
## las file (e.g. las file signature, number of point records)
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#----- public api --------------------------------------------------------------

class Datum:
    def __init__(self, name, offset, format):
        self.name = name
        self.offset = offset
        self.format = format
        self.value = None

    @property
    def size(self):
        return self.format.size

    def __repr__(self):
        return f'({self.name}, {self.value})'
