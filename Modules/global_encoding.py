##------------------------------------------------------------------------------
## Name: global_encoding.py
##
## Description: contains the GlobalEncoding class, representing a bit field
## in the header block. The GlobalEncoding class is an extension of the
## Section class
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#-----imports ------------------------------------------------------------------

from section import Section


#----- public api --------------------------------------------------------------

class GlobalEncoding(Section):
    def __init__(self):
        super().__init__()
        self.name = 'Global Encoding'
