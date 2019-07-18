# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 22:06:07 2019

@author: aa225
"""

def image_split(image):
    """
    :param image:单幅图像
    :return:单幅图像被切割后的图像list
    """
    inletter = False    #找出每个字母开始位置
    foundletter = False #找出每个字母结束位置
    start = 0
    end = 0
    letters = []    #存储坐标
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pix = image.getpixel((x, y))
            if pix != True:
                inletter = True
        if foundletter == False and inletter == True:
            foundletter = True
            start = x
        if foundletter == True and inletter == False:
            foundletter = False
            end = x
            letters.append((start, end))
        inletter = False
 
    # 因为切割出来的图像有可能是噪声点
    # 筛选可能切割出来的噪声点,只保留开始结束位置差值最大的位置信息
    subtract_array = []    # 存储 结束-开始 值
    for each in letters:
        subtract_array.append(each[1]-each[0])
    reSet = sorted(subtract_array, key=lambda x:x, reverse=True)[0:image_character_num]
    letter_chioce = []    # 存储 最终选择的点坐标
    for each in letters:
        if int(each[1] - each[0]) in reSet:
            letter_chioce.append(each)
 
    image_split_array = []    #存储切割后的图像
    for letter in letter_chioce:
        im_split = image.crop((letter[0], 0, letter[1], image.size[1])) # (切割的起始横坐标，起始纵坐标，切割的宽度，切割的高度)
        im_split = im_split.resize((image_width, image_height)) # 转换格式
        image_split_array.append(im_split)
 
     return image_split_array[0:int(image_character_num)]
