# coding=UTF-8
import csv
import random


def create_dataset(num_data, num_feature, feature_type, rule_ratio):
    dataset = []
    for i in range(num_data):
        row = []
        m=0
        f=0
        label = 0
        '''
        分數規則，期中期末平均60為1
        '''
        m = random.randint(1, num_feature)
        l = random.randint(1, num_feature)
        if((m+l)/2 > 60):
            label = 1
        else:
            label = 0
        row.append(label)
        row.append(m)
        row.append(l)
        dataset.append(row)

    # create rule!
    '''
    分數規則_計算數量
    '''
    rule_counter = 0
    for row in dataset:
        positive_flag = False
        if(((row[1] + row[2])/2 > 60) and row[0] == 1):
            positive_flag = True
        if(positive_flag):
            rule_counter += 1

    '''
    分數規則_真理
    '''
    more_rule_data = int(num_data*rule_ratio - rule_counter)

    for x in range(more_rule_data):
        tmp = []
        tmp.append(1)
        m = random.randint(1, num_feature)
        total = random.randint(60, num_feature)
        f = total*2 - m
        tmp.append(m)
        tmp.append(f)
        dataset.append(tmp)

    return dataset


if __name__ == '__main__':
    # num_data, num_feature, feature_type, rule_ratio
    dataset = create_dataset(5000, 100, 2, 0.25)
    with open('./dataset/test_data.csv', 'w') as test_file:
        csv_writer = csv.writer(test_file, delimiter=',')

        for row in dataset:
            csv_writer.writerow(row)
