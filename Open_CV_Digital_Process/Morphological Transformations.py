# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 23:12:02 2019

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

#dilation
dilation = cv2.dilate(img_2,kernel,iterations = 1)
IM(dilation)

#opening
opening = cv2.morphologyEx(img_2, cv2.MORPH_OPEN, kernel)
IM(opening)

#closing
closing = cv2.morphologyEx(img_2, cv2.MORPH_CLOSE, kernel)

gm = adjust_gamma(closing, gamma=0.3)

dst = cv.fastNlMeansDenoisingColored(gm,None,10,10,7,21)

Norm_gray = cv.cvtColor(dst, cv.COLOR_RGB2GRAY)  
IM(th3)


ret3,th3 = cv.threshold(Norm_gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

#cv2.imwrite("image_name152_output.png", Norm_gray)


#