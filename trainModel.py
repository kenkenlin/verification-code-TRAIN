# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 22:07:17 2019

@author: aa225
"""

def trainModel(data, label):
    print("fit model >>>>>>>>>>>>>>>>>>>>>>")
 
    # svc_rbf = svm.SVC(decision_function_shape='ovo',kernel='rbf')    # rbf核svc
    # svc_linear = svm.SVC(decision_function_shape='ovo',kernel='linear')    #linear核svc
    rf = RandomForestClassifier(n_estimators=100, max_depth=10,min_samples_split=10, random_state=0)    #随机森林
    scores = cross_val_score(rf, data, label,cv=10)    #交叉检验，计算模型平均准确率
    print("rf: ",scores.mean())
    rf.fit(data, label)    # 拟合模型
 
    joblib.dump(rf, model_path) # 模型持久化，保存到本地
    print("model save success!")
 
    return rf
