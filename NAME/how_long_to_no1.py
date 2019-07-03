# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:09:11 2019

@author: xzl
"""
import xlrd
import numpy as np
import csv

raw_data = xlrd.open_workbook(r'文化传递-名字.xlsx').sheet_by_name('male')

all_name = raw_data.col_values(0)
all_location = raw_data.col_values(1)
all_rank = raw_data.col_values(2)
all_year = raw_data.col_values(3)

data = np.array([all_name,all_location,all_rank,all_year])

location = list(set(data[1]))
location.sort(key=list(data[1]).index)

with open('上升到第一的时间.csv','a',newline='',encoding='gb18030')as f:
    write=csv.writer(f)
    for l in location:
        itemindex = np.argwhere(data[1] == l)
        no1 = [[],[]]
        firstappear = []
        for i in itemindex:
            if data[2][i[0]] == '1.0' and (data[0][i[0]] not in no1[0]):
                no1[0].append(data[0][i[0]])
                no1[1].append(int(float(data[3][i[0]])))
        for name in no1[0]:
            for i in itemindex:
                if data[0][i[0]] == name:
                    firstappear.append(int(float(data[3][i[0]])))
                    break
        for i in range(len(no1[0])):  
            write.writerow([no1[0][i], l, no1[1][i], no1[1][i]-firstappear[i]])
            
f.close()
        