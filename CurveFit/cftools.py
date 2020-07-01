import os
import numpy as np
import re


def read(path):
    with open(path,'r') as f:
        data = f.read()
    return data

def path_info(path):
    dir_path = os.path.dirname(path)
    file_name = os.path.splitext(os.path.basename(path))[0]
    return  (dir_path, file_name)

def get_the_var_value_from_the_file_name(fn, pattern = r'.*?\s\D*(\d+)\-?(\d*)\D*?\..*'):
    """
    This function is very specialized, and its main purps is to get a number
    from the file name. Ex: "Experiment 1 sample SX15 Energy 2uj.txt" --> float('2.0')
    ** Important the file name MUST include a Space before the value or the letters that comes before the value
       AND Dot "." after the value or the letter after the value. To write a decimel number you seperate your 
       value by "-" **
    this way you will be able to track the change in energy from the names of your file.
    gn is the group number. Note the pattern must include at least one () that return groups.
    """
    if ' ' not in fn:
        fn = ' '+fn
    if '.' not in fn:
        fn = fn+'.'
    try:
        value = float('{}.{}'.format(*re.match(pattern,fn).groups()))
    except:
        print(f'Warning! This file Name "{fn}" is not written correctly, add a space before the variable.')
        value = float(re.search('(\d+)\..*$',fn).group(1))
    return value
                

def chose_range_xy(x,y,a,b):
    i = np.where((x >= a) & (x <= b))[0]
    return(x[i],y[i])
 