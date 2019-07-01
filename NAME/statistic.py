# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 17:07:13 2019

@author: xzl
"""

import xlrd
import numpy as np


raw_data = xlrd.open_workbook(r'文化传递-名字.xlsx').sheet_by_name('no1')

all_name = raw_data.col_values(0)
all_location = raw_data.col_values(1)
all_rank = raw_data.col_values(2)
all_year = raw_data.col_values(3)

data = np.array([all_name,all_location,all_rank,all_year])

value, count = np.unique(data[0], return_counts=True)
for i in range(len(value)):
    print(value[i],count[i])