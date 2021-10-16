##------------------------------------------------------------------------------
## Name: LidarTest.py
##
## Description: script for testing the methods in the LidarDataset class. Uses
## test data and prints various metadata as well as filters the points to
## an output file
##
## Author: Ben Riegel - ben.riegel@gmail.com
##------------------------------------------------------------------------------


from lidar import LidarDataset


#function for filtering points in the lidar dataset. Point data is passed to the
#filter function via the point_record parameter. The function returns true if
#the point is kept and copied to the output file; false otherwise.
def filter_funct(point_record):
    if (point_record.return_num == 1):
        return True
    else:
        return False

lidar_dataset = LidarDataset('../Test_Data/Example_1_3.las')
lidar_dataset.print_point_format()
lidar_dataset.print_classification_codes()
lidar_dataset.print_vlrs()
lidar_dataset.print_vlr_payload(0)
lidar_dataset.print_header()
lidar_dataset.print_global_encoding()
lidar_dataset.filter_points(filter_funct, '../Output/Output.las')
out_dataset = LidarDataset('../Output/Output.las')
out_dataset.print_header()
