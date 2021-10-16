##------------------------------------------------------------------------------
## Name: b_file.py
##
## Description: contains the BinaryFile class which contains various methods
## working with binary files
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#----- imports -----------------------------------------------------------------

import os


#----- private code block ------------------------------------------------------

def get_mode_code(mode):
    if mode == 'read':
        return 'r'
    elif mode == 'write':
        return 'w'
    else:
        print('error')


#----- public api --------------------------------------------------------------

class BinaryFile:

    def __init__(self, file):
        self._name = file
        self._file_obj = None

    def close(self):
        self._file_obj.close()

    def get_file_size(self):
        file_size = os.path.getsize(self._name)
        return file_size

    def open(self, mode):
        mode_code = get_mode_code(mode)
        mode_str = mode_code + 'b'
        self._file_obj = open(self._name, mode_str)

    def open_and_do(self, mode, funct, *args):
        mode_code = get_mode_code(mode)
        mode_str = mode_code + 'b'
        with open(self._name, mode_str) as f:
            self._file_obj = f
            result = funct(self, *args)
            return result

    def read_bytes(self, num_bytes):
        bytes = self._file_obj.read(num_bytes)
        return bytes

    def set_offset(self, new_offset):
        current_offset = self._file_obj.tell()
        if current_offset != new_offset:
            self._file_obj.seek(new_offset)

    def write_bytes(self, bytes):
        self._file_obj.write(bytes)
