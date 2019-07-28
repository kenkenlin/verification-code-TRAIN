import cv2 as cv
import cv2
import numpy as np
from matplotlib import pyplot as plt 


def contours_demo(image):
    dst = cv.GaussianBlur(image, (3, 3), 0) #高斯模糊去噪 
    gray = cv.cvtColor(dst, cv.COLOR_RGB2GRAY)
    ret, binary = cv.threshold(gray, 170, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU) #用大律法、全局自適應閾值方法進行圖像二值化 
    gus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 170, 1)
#    cv.imshow("binary image", binary)
    plt.imshow(image)
    plt.imshow(binary)
    plt.imshow(gus)
    contours, heriachy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    print( "there are " + str(len(contours)) + " contours")
    for i, contour in enumerate(contours):
        cv.drawContours(image, [contour], 0, (0, 0, 255), 2)
        print(i)
    plt.imshow( image)
#    for i, contour in enumerate(contours):
#        cv.drawContours(image, [contour], 0, (0, 0, 255), -1)
#    plt.imshow("pcontours", image)
    
    
def main():
    image = cv.imread("D:\\Users\\Jack\\Documents\\GitHub\\Open_CV_Digital_Process\\image_name124.jpg")
#    cv.namedWindow('input_image', cv.WINDOW_NORMAL) #設置為WINDOW_NORMAL可以任意縮放
    plt.imshow( image1)
    contours_demo(image1)

if __name__ == '__main__':
    main()
    
    
