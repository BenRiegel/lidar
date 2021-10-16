##------------------------------------------------------------------------------
## Name: view_ctrl.py
##
## Description: contains methods for printing various metadata
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#-----imports ------------------------------------------------------------------

from view import print_column_2, print_column_3


#----- private code block ------------------------------------------------------

def print_section_data(data):
    c1 = []
    c2 = []
    for datum in data:
        c1.append(datum.name)
        value_str = str(datum.value)
        value_str = value_str.replace('(', '')
        value_str = value_str.replace(')', '')
        c2.append(value_str)
    print_column_2(c1, c2)

def print_data_2(data):
    c1 = []
    c2 = []
    for datum in data:
        c1.append(datum[0])
        c2.append(datum[1])
    print_column_2(c1, c2)


#----- public api --------------------------------------------------------------

def print_header(file, header):
    print('Printing header for ' + file)
    print_section_data(header.data.values())

def print_global_encoding(file, global_encoding):
    print('Printing global encoding for ' + file)
    print_section_data(global_encoding.data.values())

def print_vlr_block(file, vlr_block):
    print('Printing vlr section for ' + file)
    for i in range(0,len(vlr_block.records)):
        print(f'Printing record {i}')
        vlr = vlr_block.records[i]
        vlr_section = vlr.data.values()
        print_section_data(vlr_section)

def print_class_codes(file, point_format, class_codes):
    print('Printing classification codes for ' + file)
    print(f'Classification codes for point format {point_format}:')
    c1 = ['Num']
    c2 = ['Description']
    for code in class_codes:
        c1.append(code[0])
        c2.append(code[1])
    print_column_2(c1, c2)

def print_point_format(file, point_format, schema):
    print(f'Printing point format {point_format} for ' + file)
    c1 = ['Key']
    c2 = ['Name']
    c3 = ['Format']
    for schemata in schema:
        c1.append(schemata[0])
        c2.append(schemata[1])
        c3.append(schemata[2])
    print_column_3(c1, c2, c3)

def print_vlr_payload(file, num, payload):
    print(f'Printing vlr record {num} in ' + file)
    print(payload)
