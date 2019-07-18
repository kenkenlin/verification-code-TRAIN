# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 21:59:02 2019

@author: aa225
"""

def image_transfer(image_arry):
    """
    :param image_arry:图像list，每个元素为一副图像
    :return: image_clean:清理过后的图像list
    """
    image_clean = []
    for i, image in enumerate(image_arry):
        image = image.convert('L') # 转换为灰度图像，即RGB通道从3变为1
        im2 = Image.new("L", image.size, 255)
        for y in range(image.size[1]): # 遍历所有像素，将灰度超过阈值的像素转变为255（白）
            for x in range(image.size[0]):
                pix = image.getpixel((x, y))
                if int(pix) > threshold_grey:  # 灰度阈值
                    im2.putpixel((x, y), 255)
                else:
                    im2.putpixel((x, y), pix)
        image_clean.append(im2)
    return image_clean
