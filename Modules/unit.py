##------------------------------------------------------------------------------
## Name: unit.py
##
## Description: contains the Unit class which is used to keep track of file
## offset values, data sizes, etc. in both bytes and bits. Includes methods
## for adding and multiplying values with both bytes and bits
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#----- imports -----------------------------------------------------------------

import math


#----- private code block ------------------------------------------------------

def calc_total_bits(bytes, bits):
    return bytes * 8 + bits

def convert_bits(bits):
    new_bytes = math.trunc(bits / 8)
    new_bits = bits % 8
    return Unit(new_bytes, new_bits)


#----- public api --------------------------------------------------------------

class Unit:
    def __init__(self, bytes, bits=0):
        self.bytes = bytes
        self.bits = bits

    def __add__(self, unit2):
        total_bits_self = calc_total_bits(self.bytes, self.bits)
        total_bits_unit2 = calc_total_bits(unit2.bytes, unit2.bits)
        sum_bits = total_bits_self + total_bits_unit2
        new_unit = convert_bits(sum_bits)
        return new_unit

    def __mul__(self, value):
        total_bits_self = calc_total_bits(self.bytes, self.bits)
        product_bits = total_bits_self * value
        new_unit = convert_bits(product_bits)
        return new_unit

    def __repr__(self):
        return f'({self.bytes}, {self.bits})'

    def copy(self):
        return Unit(self.bytes, self.bits)
