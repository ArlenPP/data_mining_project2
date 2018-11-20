# coding=UTF-8
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import csv
import numpy as np
import matplotlib.pyplot as plt
# import graphviz

if __name__ == "__main__":
    
    X = []
    Y = []
    # reader data
    # note!! the type will become string need to trange to int
    with open('./dataset/test_data.csv', 'r') as data_file:
        data_reader = csv.reader(data_file)
        for row in data_reader:
            tmp =[]
            for i,v in enumerate(row):
                if(i == 0):
                    Y.append(int(v))
                else:
                    tmp.append(int(v))
            X.append(tmp)

    # create clf
    clf = tree.DecisionTreeClassifier()
    
    train_x, test_x, train_y, test_y = train_test_split(np.array(X), np.array(Y), test_size=0.3, random_state=168) 

    # fit data
    
    clf.fit(train_x, train_y)
    # clf.fit(train_x,
    #         train_y,
    #         eval_set=[(test_x, test_y)],
    #         eval_metric="mlogloss",
    #         early_stopping_rounds=10,
    #         verbose=True)
    predict_y = clf.predict(test_x)

    # cal score
    score = accuracy_score(test_y, predict_y)
    print(score)

    # rule score
    # rule_total = 0
    # correct = 0
    # for row, pred_ans in zip(test_x, predict_y):
    #     flag = True
    #     for i, v in enumerate(row):
    #         if(i+1 != v):
    #             flag = False
    #     if(flag):
    #         if(pred_ans == 1):
    #             correct += 1
    #         rule_total += 1

    # print("rule score %d" % (correct/rule_total))

    #畫圖
    xx, yy = np.meshgrid(np.arange(1, 100, 0.1), np.arange(1, 100, 0.1))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.subplots(1, 1, figsize=(4, 4))  # figsize 設定大小
    plt.xlabel("middle")  # x 座標名稱
    plt.ylabel("final")  # y 座標名稱
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
    plt.show()
    # graphviz
    # dot_data = tree.export_graphviz(clf, out_file=None)
    # graph = graphviz.Source(dot_data)
