# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 03:05:33 2019

@author: Jack
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt 
 
im = cv2.imread('test3.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print "there are " + str(len(contours)) + " contours"
 
cnt = contours[0]
print "there are " + str(len(cnt)) + " points in contours[0]"
approx = cv2.approxPolyDP(cnt,30,True)
print "after approx, there are " + str(len(approx)) + " points"
print approx
cv2.drawContours(im,[approx],0,(255,0,0),-1)
 
 
cnt = contours[1]
print "there are " + str(len(cnt)) + " points in contours[1]"
approx = cv2.approxPolyDP(cnt,30,True)
print "after approx, there are " + str(len(approx)) + " points"
print approx
cv2.drawContours(im,[approx],0,(0,255,0),-1)
 
cv2.imshow('im', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.imshow(im)
