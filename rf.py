# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 22:07:43 2019

@author: aa225
"""

import os
from captcha_test.captcha_soc import image_process, image_feature, image_model, image_training
from sklearn.externals import joblib
from captcha_test.captcha_soc.config import *
 
 
#验证码数据清洗
def clean():
    #验证码清理
    image_array, image_label = image_process.read_captcha(test_data_path) #读取待测试验证码文件
    print("待测试的验证码数量：", len(image_array))
    image_clean = image_process.image_transfer(image_array) #转换成灰度图像，并去除背景噪声
    image_array = [] #[[im_1_1,im_1_2,im_1_3,im_1_4],[im_2_1,im_2_2,im_2_3,im_2_4],...]
    for each_image in image_clean:
        image_out = image_process.get_clear_bin_image(each_image) #转换为二值图片，并去除剩余噪声点
        split_result = image_process.image_split(image_out) #切割图片
        image_array.append(split_result)
    return image_array, image_label
 
 
#特征矩阵生成
def featrue_generate(image_array):
    feature = []
    for num, image in enumerate(image_array):
        feature_each_image = []
        for im_meta in image:
            fea_vector = image_feature.feature_transfer(im_meta)
            # print('label: ',image_label[num])
            # print(feature)
            feature_each_image.append(fea_vector)
            # print(fea_vector)
        # print(len(feature_each_image))
        if len(feature_each_image) == 0:
            feature_each_image = [[0]*(image_width+image_height)]*int(image_character_num)
        # print(feature_each_image)
        feature.append(feature_each_image)
    print("预测数据的长度:", len(feature))
    print("预测数据特征示例:", feature[0])
    return feature
 
 
#将结果写到文件
def write_to_file(predict_list):
    file_list = os.listdir(test_data_path)
    with open(output_path, 'w') as f:
        for num, line in enumerate(predict_list):
            if num == 0:
                f.write("file_name\tresult\n")
            f.write(file_list[num] + '\t' + line + '\n')
    print("结果输出到文件：", output_path)
 
def main():
    #验证码清理
    image_array, image_label = clean()
    #特征处理
    feature = featrue_generate(image_array)
    #预测
    predict_list = []
    acc = 0
    model = joblib.load(model_path)    #读取模型
    # print("预测错误的例子：")
    for num, line in enumerate(feature):
        # print(line)
        predict_array = model.predict(line)
        predict = ''.join(predict_array)
        predict_list.append(predict)
        if predict == image_label[num]:
            acc += 1
        else:
            pass
            print("-----------------------")
            print("actual:",image_label[num])
            print("predict:", predict)
    print("测试集预测acc：", acc/len(image_label))
    #输出到文件
    write_to_file(predict_list)
 
if __name__ == '__main__':
    main()
