# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 18:28:36 2019

@author: Jack
"""
import cv2 
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt 

def IM(image):
    cv2.imshow('ImageWindow', image)
    cv2.waitKey()
    
def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
 
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

img_2 = cv2.imread("D:\\Users\\Jack\\Documents\\GitHub\\Open_CV_Digital_Process\\image_name152.jpg")

kernel = np.ones((3,3),np.uint8)

#擴張後腐蝕
closing = cv2.morphologyEx(img_2, cv2.MORPH_CLOSE, kernel)

#非線性亮度調整, gamma>0
gm = adjust_gamma(closing, gamma=0.3)
#cv去雜訊函數
dst = cv.fastNlMeansDenoisingColored(gm,None,10,10,7,21)

Norm_gray = cv.cvtColor(dst, cv.COLOR_RGB2GRAY)

ret3,th3 = cv.threshold(Norm_gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
IM(th3)


#寫出
#cv2.imwrite("image_name152_output.png", Norm_gray)
