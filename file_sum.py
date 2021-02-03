# Author: Adam Jeffries
# Date: 2/3/2021
# Description: Function that sums a list of values in a text file.

def file_sum(file_name):
    num_file = open(file_name, 'r')
    lines = num_file.readlines()
    val = 0
    for line in lines:
        val = val + float(line)
    sum_file = open('sum.txt', 'w')
    sum_file.write(str(val))
    sum_file.close()
