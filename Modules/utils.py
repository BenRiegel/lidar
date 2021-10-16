##------------------------------------------------------------------------------
## Name: utils.py
##
## Description: contains the EmptyClass class as well as other various
## other utility methods
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------



#-----imports ------------------------------------------------------------------

from datetime import datetime
import csv


#----- public api --------------------------------------------------------------

class EmptyClass:
    pass

def get_csv_lines(csv_file):
    new_lines = []
    with open(csv_file, 'r', newline='') as csv_file_obj:
        lines = csv.reader(csv_file_obj, dialect='excel')
        next(lines)
        for line in lines:
            new_lines.append(line)
    return new_lines

def trim_list(list):
    if len(list) == 1:
        return list[0]
    else:
        return list

def get_current_year():
    now_time = datetime.now().timetuple()
    now_year = now_time.tm_year
    return now_year

def get_current_day_of_year():
    now_time = datetime.now().timetuple()
    now_day_of_year = now_time.tm_yday
    return now_day_of_year

def null_terminate_str(str, target_len):
    str_len = len(str)
    len_dif = target_len - str_len
    buffer = len_dif * '\0'
    new_str = str + buffer
    return new_str
