##------------------------------------------------------------------------------
## Name: header.py
##
## Description: contains the Header class, representing the header block
## in the las file. The Header class is an extension of the Section class
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#----- imports -----------------------------------------------------------------

from unit import Unit
from section import Section


#----- public api --------------------------------------------------------------

class Header(Section):
    def __init__(self):
        super().__init__()
        self.name = 'Header'
        self.offset = Unit(0)
