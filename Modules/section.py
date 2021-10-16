##------------------------------------------------------------------------------
## Name: section.py
##
## Description: contains the Section class, representing one block of data (e.g.
## all the data in the header block, or a point record
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#----- imports -----------------------------------------------------------------

from unit import Unit


#----- public api --------------------------------------------------------------

class Section:
    def __init__(self):
        self.name = None
        self.offset = None
        self.data = {}
        self.size = Unit(0)

    def add_datum(self, key, datum):
        self.data[key] = datum

    def get_datum(self, key):
        return self.data[key]

    def get_datum_value(self, key):
        return self.data[key].value

    def increment_size(self, delta_size):
        self.size += delta_size
