# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:34:01 2019

@author: lenovo
"""
from PIL import Image
import os

imglist = os.listdir("./logo/")

for img_name in imglist:
    img_path = "./logo/" + img_name 
    if img_name[-3:] == "png" or img_name[-3:] =="PNG":
        img = Image.open(img_path)
        x,y = img.size 
        try: 
            # 使用白色来填充背景
            # (alpha band as paste mask). 
            new_png = Image.new('RGBA', img.size, (255,255,255))
            new_png.paste(img, (0, 0, x, y), img)
            new_png.save("./replace/"+img_name)
        except:
            pass
print("Conversion Success.")