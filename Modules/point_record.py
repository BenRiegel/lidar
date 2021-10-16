##------------------------------------------------------------------------------
## Name: point_record.py
##
## Description: contains the PointRecord class, includes all the data in
## a point record. It is an extension of the Section class
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#-----imports ------------------------------------------------------------------

from section import Section


#----- public api --------------------------------------------------------------

class PointRecord(Section):
    def __init__(self):
        super().__init__()
        self.name = 'Point Record'
