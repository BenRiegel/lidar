##------------------------------------------------------------------------------
## Name: las.py
##
## Description: contains the LASFile class which is an extension of the
## BinaryFile class. It includes a decoder and encoder which are used to
## convert python data structures (numbers, lists, etc) to and from
## binary data
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#----- imports------------------------------------------------------------------

from b_file import BinaryFile
from b_decode import Decoder
from b_encode import Encoder
from unpack import LITTLE_ENDIAN_CODE


#----- private code block ------------------------------------------------------

LAS_ENDIAN_CODE = LITTLE_ENDIAN_CODE


#----- public api --------------------------------------------------------------

class LASFile(BinaryFile):

    def __init__(self, file):
        super().__init__(file)
        self.decoder = Decoder(LAS_ENDIAN_CODE)
        self.encoder = Encoder(LAS_ENDIAN_CODE)

    def read_datum(self, offset, format):
        self.decoder.reset()
        self.decoder.add_record(format)
        self.set_offset(offset.bytes)
        block_size = self.decoder.get_block_size()
        bytes = self.read_bytes(block_size)
        data = self.decoder.decode_bytes(bytes)
        return data

    def write_datum(self, offset, format, value):
        self.set_offset(offset.bytes)
        bytes = self.encoder.encode_value(value, format)
        self.write_bytes(bytes)
