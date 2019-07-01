# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:52:23 2019

@author: xzl
"""
import matplotlib.image as mpimg
from PIL import Image
import numpy as np
import os

imglist = os.listdir("./pics/")

for img_name in imglist:
    img_path = "./pics/" + img_name   # 拼出图片全路径
    if img_name[-3:] == ("png" or "PNG"):
        img_png =Image.open(img_path)
        img = img_png.convert("RGB")
        img_arr=np.array(img)
    else:
        img = mpimg.imread(img_path)
        img_arr = np.array(img) 
    
    purity = 230
    not_white = 0
    not_bg = 0
    min_left = float("inf")
    max_right = 0
    start_row = 0
    end_row = 0 
    it = 0
    for row in img_arr:
        shape = np.where(row < [purity, purity, purity])
        it += 1
        value, count = np.unique(shape[0], return_counts=True)
        not_white_index = []
        for i in range(len(value)):
            if count[i] == 3:
                not_white_index.append(value[i])
        if len(not_white_index) != 0:
            if start_row == 0:
                start_row = it;
            if end_row >= 0:
                end_row = it;
            left = not_white_index[0]
            right = not_white_index[-1]
            if left < min_left:
                min_left = left
            if right > max_right:
                max_right = right
            not_white += len(not_white_index)
    shape_row = end_row - start_row + 1  # 外轮廓的行数
    shape_col = max_right - min_left + 1  # 外轮廓的列数
    not_bg = shape_row*shape_col
       
    print(img_name + ":")
    
    print("white percentage: " + str(1 - not_white/not_bg))
    
    print("Purity of White: " + str(purity / 255))
        
