# coding=UTF-8
import csv
import random

def create_dataset(num_data, num_feature, feature_type, rule_ratio):
    dataset = []
    for i in range(num_data):
        row = []
        # label is 0, 1
        row.append(random.randint(0,1))
        '''
        簡單的規則
        '''
        # for feature in range(num_feature):
        #     # feature is 1~feature_type
        #     row.append(random.randint(1,feature_type))
        '''
        面積
        '''
        l = random.randrange(1, num_feature, 1)
        a = random.randrange(1, num_feature*num_feature)
        row.append(l)
        row.append(a)
        dataset.append(row)
    # create rule!
    '''
    簡單規則_計算數量
    '''
    # rule_counter = 0
    # for row in dataset:
    #     positive_flag = True
    #     for i in range(num_feature):
    #         if(row[i+1] != i+1):
    #             positive_flag = False
    #     if(positive_flag):
    #         row[0] = 1
    #         rule_counter += 1

    '''
    面積_計算數量
    '''
    rule_counter = 0
    for row in dataset:
        positive_flag = False
        if(row[0]*row[0] == row[1]):
            positive_flag = True
        if(positive_flag):
            row[0] = 1
            rule_counter += 1

    '''
    面積_真理
    '''
    more_rule_data = int(num_data*rule_ratio - rule_counter)
    for x in range(more_rule_data):
        tmp = []
        tmp.append(1)
        l = random.randrange(1, num_feature, 1)
        tmp.append(l)
        tmp.append(l*l)
        dataset.append(tmp)
    '''
    簡單規則_真理
    '''
    # more_rule_data = int(num_data*rule_ratio - rule_counter)

    # for x in range(more_rule_data):
    #     tmp = []
    #     tmp.append(1)
    #     for i in range(num_feature):
    #         tmp.append(i+1)
    #     dataset.append(tmp)

    return dataset

if __name__ == '__main__':
    # num_data, num_feature, feature_type, rule_ratio
    dataset = create_dataset(50000, 30, 2, 10)
    with open('./dataset/test_data.csv', 'w') as test_file:
        csv_writer = csv.writer(test_file, delimiter=',')
        
        for row in dataset:
            csv_writer.writerow(row)
