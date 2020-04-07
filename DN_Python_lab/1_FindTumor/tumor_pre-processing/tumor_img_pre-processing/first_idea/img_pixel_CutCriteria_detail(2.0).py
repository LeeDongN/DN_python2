import cv2 as cv
import numpy as np
import math
import glob
import time


#이미지에 대한 기준값 x, y의 fixed 값을 받아서 grayscare 값 얻어냄
def pixel_CutCriteria_detail(cut_len, img_gray_pixel_CutCriteria, width, height, img_gray):
    
    y_R_line = []
    x_R_line = []
    
    for i_cut_len in range(0, cut_len):
        
        y_fixed = img_gray_pixel_CutCriteria[i_cut_len][0]
        x_fixed = img_gray_pixel_CutCriteria[i_cut_len][1]
        y_r_line = []
        
        for i_x in range(0, width):
            
            criteria_pixel_x = img_gray.item(y_fixed, i_x)
        
            y_line = []
            y_line.append(y_fixed)
            y_line.append(i_x)
            y_line.append(criteria_pixel_x)
            
            y_r_line.append(y_line)
            
            y_R_line.append(y_r_line)
    
    
        for i_y in range(0, height):
        
            criteria_pixel_y = img_gray.item(i_y, x_fixed)
        
            x_line = []
            x_line.append(i_y)
            x_line.append(criteria_pixel_y)
        
            x_R_line.append(x_line)

