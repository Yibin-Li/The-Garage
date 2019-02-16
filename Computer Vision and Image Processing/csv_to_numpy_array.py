import numpy as np
import csv

def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    count = 0
    total_list = []
    for row in reader:
        count += 1
        if count > 1:
            total_list.append(row)
    return total_list
file_name = input("File name:")
f = open(file_name)
lst = csv_reader(f)
"""
each index in lst is a picture, each pictures has lindex
from 0 to 24
0: img_name
1: turret_left_front
2: tlf_x
3: tlf_y
4: left_back_wheel
5: lbw_x
6: lbw_y
7: turret_left_back
8: tlb_x
9: tlb_y
10: left_front_wheel
11: lfw_x
12: lfw_y
13: turret_right_back
14: trb_x
15: trb_y
16: right_front_wheel
17: rfw_x
18: rfw_y
19: turrent_right_front
20: trf_x
21: trf_y
22: back_right_wheel
23: brw_x
24: brw_y"""
np.array(lst).dump(open('array.npy', 'wb'))
print("done")
