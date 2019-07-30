# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 21:49:06 2019

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
    
img_2 = cv2.imread("D:\\Users\\Jack\\Documents\\GitHub\\Open_CV_Digital_Process\\image_name150.jpg")  



#
gm1 = adjust_gamma(img_2, gamma=0.1)#gamma = 0.5,1,1.5...
gm2 = adjust_gamma(img_2, gamma=0.2)
gm3 = adjust_gamma(img_2, gamma=0.3)
gm4 = adjust_gamma(img_2, gamma=0.4)
gm5 = adjust_gamma(img_2, gamma=0.5)
gm6 = adjust_gamma(img_2, gamma=0.6)
gm7 = adjust_gamma(img_2, gamma=0.7)
gm8 = adjust_gamma(img_2, gamma=0.8)
gm9 = adjust_gamma(img_2, gamma=0.9)
gm10 = adjust_gamma(img_2, gamma=1)
#gm_res = np.hstack((img_2,gm1,gm2,gm3,gm4,gm5,gm6,gm7,gm8,gm9,gm10,gm5_1))
#IM(gm_res)

gm5_1 = adjust_gamma(gm5, gamma=0.6)
ret, binary = cv.threshold(gm5_1, 127, 255, cv.THRESH_BINARY_INV)
ret, binary_2 = cv.threshold(binary, 127,255, cv2.THRESH_BINARY_INV)
IM(binary_2)

binary_3 = cv2.cvtColor(binary_2, cv2.COLOR_BGR2GRAY);
blur = cv.GaussianBlur(binary_3,(5,7),0)
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)


contours, heriachy = cv.findContours(th3, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print( "there are " + str(len(contours)) + " contours")


IM(th3)








