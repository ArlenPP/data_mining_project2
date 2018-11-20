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
            tmp = []
            for i, v in enumerate(row):
                if(i == 0):
                    Y.append(int(v))
                else:
                    tmp.append(int(v))
            X.append(tmp)

    # create clf
    clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
    train_x, test_x, train_y, test_y = train_test_split(
        np.array(X), np.array(Y), test_size=0.3, random_state=168)

    # fit data

    clf.fit(train_x, train_y)
    predict_y = clf.predict(test_x)

    # cal score
    score = accuracy_score(test_y, predict_y)
    print(score)


    #畫圖
    xx, yy = np.meshgrid(np.arange(1, 100, 0.1), np.arange(1, 100, 0.1))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.subplots(1, 1, figsize=(4, 4))  # figsize 設定大小
    plt.xlabel("middle")  # x 座標名稱
    plt.ylabel("final")  # y 座標名稱
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
    plt.show()

