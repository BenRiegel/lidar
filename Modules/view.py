##------------------------------------------------------------------------------
## Name: view.py
##
## Description: contains methods for printing data in columns
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#----- private code block ------------------------------------------------------

def get_max_str_len(items):
    max_str_len = 0
    for item in items:
        str_len = len(item)
        if str_len > max_str_len:
            max_str_len = str_len
    return max_str_len


#----- public api --------------------------------------------------------------

def print_column_2(c1, c2):
    col_width = get_max_str_len(c1)
    for i in range(0, len(c1)):
        str_len = len(c1[i])
        padding_len = col_width - str_len
        padding_str = ' ' * padding_len
        print(c1[i] + padding_str + ' : ' + c2[i])

def print_column_3(c1, c2, c3):
    col_width1 = get_max_str_len(c1)
    col_width2 = get_max_str_len(c2)
    for i in range(0, len(c1)):
        str_len1 = len(c1[i])
        padding_len = col_width1 - str_len1
        padding_str = ' ' * padding_len
        str = c1[i] + padding_str + ' ' + c2[i]
        str_len2 = len(c2[i])
        padding_len = col_width2 - str_len2
        padding_str = ' ' * padding_len
        str += padding_str + ' ' + c3[i]
        print(str)
