# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:56:40 2019

@author: 
"""

import xlrd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.mplot3d import Axes3D

raw_data = xlrd.open_workbook(r'文化传递-名字.xlsx').sheet_by_name('male')

all_name = raw_data.col_values(0)
all_location = raw_data.col_values(1)
all_rank = raw_data.col_values(2)
all_year = raw_data.col_values(3)

data = np.array([all_name,all_location,all_rank,all_year])

name = r'建国'
liansheng = np.where(data[0] == name)

location = []
weight = []
year = []
for i in liansheng[0]:
    location.append(data[1][i])
    weight.append(21-int(float(data[2][i])))
    year.append(int(float(data[3][i])))

year_min = min(year)
year_max = max(year)
time_axix = range(year_min, year_max+1)# 连续数列，防止有几年的跨度

loc_axix = list(set(location))

city_weight = [] 
for i in range(len(loc_axix)):
    city_weight.append([0 for i in range(len(time_axix))])

for i in range(len(location)):
    for j in range(len(loc_axix)):
        if location[i] == loc_axix[j]:
            city_weight[j][year[i]-time_axix[0]]=weight[i]

'''消失之后重新返回前20的不计算在内'''
for city in city_weight:
    for i in range(len(city)):
        if city[i] > 0:
            first = i;
            break
    for i in range(first,len(city)):
        if city[i] == 0:
            first_disappear = i;
            break
    for i in range(first_disappear,len(city)):
        city[i] = 0;
           
 
color = ['aquamarine','bisque','black','blanchedalmond','blue','blueviolet','brown','burlywood','cadetblue','chartreuse','chocolate','coral','cornflowerblue','cornsilk','crimson','cyan','darkblue','darkcyan','darkgoldenrod','darkgray','darkgreen','darkkhaki','darkmagenta','darkolivegreen','darkorange','darkorchid','darkred','darksalmon','darkseagreen','darkslateblue','darkslategray','darkturquoise','darkviolet','deeppink','deepskyblue','dimgray','dodgerblue','gainsboro','gold','gray','green','greenyellow','hotpink','indianred','khaki','lavender','lightsteelblue','magenta','mediumaquamarine','navajowhite','navy''oldlace','orange','palegoldenrod','pink','purple','red','springgreen','steelblue','tomato','turquoise','violet','whitesmoke','yellow','yellowgreen']
#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(20, 8))

plt.title('各地区每年名字“'+name+'”的权重变化')
ax=plt.subplot(111, projection='3d')
for i in range(len(loc_axix)):
    if loc_axix[i] == "北京市":
        ax.plot(time_axix, [i for k in range(len(time_axix))], city_weight[i], color='#000000', linestyle='--', label=loc_axix[i])
    elif loc_axix[i]== "上海市":
        ax.plot(time_axix, [i for k in range(len(time_axix))], city_weight[i], color='#000000', linestyle=':', label=loc_axix[i])
    elif loc_axix[i] == "广东省":
        ax.plot(time_axix, [i for k in range(len(time_axix))], city_weight[i], color='#000000', linestyle='-.', label=loc_axix[i])
    else:             
        ax.plot(time_axix, [i for k in range(len(time_axix))], city_weight[i], color=color[i], label=loc_axix[i])

plt.legend(loc='upper left') # 显示图例
'''
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.yaxis.set_major_locator(MultipleLocator(2))
ax.zaxis.set_major_locator(MultipleLocator(2))
'''
#plt.zlim(0,21)#把y轴的刻度范围设置为1到20
plt.show()

