# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:48:00 2019

@author: lenovo
"""

'''
留白的定义：RGB三个值都大于200，认定为留白区域
'''
import matplotlib.image as mpimg
from PIL import Image
import numpy as np
import os


'''判断y方向上是否封闭'''
def is_closed_y(previous_left, previous_right, left, right):
    if left is None:
        return True
    if left > previous_right:
        return False
    if right < previous_left:
        return False
    return True    

imglist = os.listdir("./pics/")

for img_name in imglist:
    img_path = "./pics/" + img_name   # 拼出图片全路径
    if img_name[-3:] == "png" or img_name[-3:] =="PNG":
        img_png =Image.open(img_path)
        img = img_png.convert("RGB")
        img_arr=np.array(img)
    elif  img_name[-3:] == "gif" or img_name[-3:] == "GIF":
        img_gif =Image.open(img_path)
        img = img_gif.convert("RGB")
        img_arr=np.array(img)
    else:
        img = mpimg.imread(img_path)
        img_arr = np.array(img) 
    
    purity = 200
    not_white = 0
    not_bg = 0
    min_left = float("inf")
    max_right = 0
    start_row = 0
    end_row = 0 
    it = 0
    is_closed_or_not_y = True
    is_closed_or_not_x = True
    valid_row = 0
    closed_size = 0
    for row in img_arr:
        shape = np.where(row < [purity, purity, purity])
        it += 1
        value = np.unique(shape[0], return_counts=False)
        not_white_index = []
        for i in range(len(value)):
            not_white_index.append(value[i])
        
        if valid_row != 0 and valid_row != 1:
            if end_row <= it - 2 and len(not_white_index) != 0:
                is_closed_or_not_y = False
            
        if start_row != 0 and is_closed_or_not_y is True and it == end_row + 1:
            if len(not_white_index) == 0:
                is_closed_or_not_y = is_closed_y(previous_left, previous_right, None, None)
            else:
                is_closed_or_not_y = is_closed_y(previous_left, previous_right, not_white_index[0], not_white_index[-1])
                closed_size += not_white_index[-1] - not_white_index[0] + 1
                previous_left = not_white_index[0]
                previous_right = not_white_index[-1]
        
        if len(not_white_index) != 0:
            valid_row += 1
            if start_row == 0:
                start_row = it;
                previous_left = not_white_index[0]
                previous_right = not_white_index[-1]
                closed_size += previous_right -previous_left + 1
                if not_white_index[-1] - not_white_index[0] + 1 != len(not_white_index):
                    is_closed_or_not_x = False
            if end_row >= 0:
                end_row = it;
            left = not_white_index[0]
            right = not_white_index[-1]
            if left < min_left:
                min_left = left
            if right > max_right:
                max_right = right
            not_white += len(not_white_index)
    
    if end_row == 0:
        print(img_name + ":全白")
        print("------------------------")
    else: 
        '''判断非留白区域的最后一行是否封闭'''
        last_row = img_arr[end_row-1]
        last_row_shape = np.where(last_row < [purity, purity, purity])
        value = np.unique(last_row_shape[0], return_counts=False)
        not_white_index = []
        for i in range(len(value)):
            not_white_index.append(value[i])
        if not_white_index[-1] - not_white_index[0] + 1 != len(not_white_index):
            is_closed_or_not_x = False
        
        '''分类计算封闭图形和非封闭图形的图案总面积'''
        if is_closed_or_not_y is True and is_closed_or_not_x is True:
            not_bg = closed_size
        else:
            shape_row = end_row - start_row + 1  # 外轮廓的行数
            shape_col = max_right - min_left + 1  # 外轮廓的列数
            not_bg = shape_row*shape_col
        
        '''打印结果'''
        print(img_name + ":")
        print("white percentage: %.4f" % (1 - not_white/not_bg))
        print("Purity of White:  %.4f" % (purity / 255))
        print("------------------------")