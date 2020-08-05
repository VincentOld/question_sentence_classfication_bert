
import pandas as pd


# 读取txt文件
# def read_txt_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         content = [_.strip() for _ in f.readlines()]
#
#     labels, texts = [], []
#     for line in content:
#         parts = line.split()
#         label, text = parts[0], ''.join(parts[1:])
#         labels.append(label)
#         texts.append(text)
#
#     return labels, texts
#
#
# file_path = 'data/train - 1200.txt'
# labels, texts = read_txt_file(file_path)
# train_df = pd.DataFrame({'label': labels, 'text': texts})
#
# file_path = 'data/test.txt'
# labels, texts = read_txt_file(file_path)
# test_df = pd.DataFrame({'label': labels, 'text': texts})
import numpy as np
from sklearn.model_selection import KFold
f=open("data/train/train_20000.csv", 'r',encoding="UTF-8")
data = pd.read_csv(f,error_bad_lines=False,sep='\t')
# print(type(data))//df
data = np.array(data)
# data=random.shuffle(data)
kf = KFold(n_splits=5,shuffle=True)
for train, test in kf.split(data):
    train=data[train]
    test=data[test]
    # print('train:%s' %data[train])
    # print('test:%s' %data[test])
    # print(type(train))
    train_df=pd.DataFrame(train,columns=["text","label"])
    test_df=pd.DataFrame(test,columns=["text","label"])
    print(train_df.head())
    print(test_df.head())
#
    train_df['text_len'] = train_df['text'].apply(lambda x: len(x))
    print(train_df.describe())

