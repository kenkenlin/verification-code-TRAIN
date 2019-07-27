#-*- coding:utf-8 -*

import os
os.getcwd()
#'D:\\Users\\Jack\\Documents\\GitHub\\verification-code-TRAIN\\captcha_ml'
#原始路径
global path
path = os.getcwd()
#训练集原始验证码文件存放路径
captcha_path = path + '/data/captcha'
#训练集验证码清理存放路径
captcha_path_clean_path = path + '/data/captcha_clean'
#训练集存放路径
global train_data_path
train_data_path = path + '/data/training_data'
#模型存放路径
model_path = path + '/data/model/model.model'
#测试集原始验证码文件存放路径
test_data_path = path + '/data/test_data'
#测试结果存放路径
output_path = path + '/data/result/result.txt'

#识别的验证码个数
image_character_num = 6

#图像粗处理的灰度阈值
threshold_grey = 300

#标准化的图像大小
image_width = 15
image_height = 33

