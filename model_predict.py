import pandas as pd
import numpy as np
from bert.extract_feature import BertVector
from keras.models import load_model
from InputPassage_OutputSentence import outfile
load_model = load_model("model/question_sentence_classify_20000.h5")

# 预测语句
f=open(outfile,encoding="UTF-8")
texts=[]
for line in f.readlines():
    texts.append(line.strip())
labels = []
true_posibilities=[]
bert_model = BertVector(pooling_strategy="REDUCE_MEAN", max_seq_len=70)

# 对上述句子进行预测
for text in texts:
    # 将句子转换成向量
    vec = bert_model.encode([text])["encodes"][0]
    x_train = np.array([vec])
    # 模型预测
    predicted = load_model.predict(x_train)
    # print("predicted:",predicted)
    y = np.argmax(predicted[0])
    print("y:",y)
    label = '1' if y else '0'
    true_posibility=predicted[0][1]
    # if y==1:
    #     posibility = predicted[0][1]
    #     true_posibilities.append(true_posibility)
    # else:
    #     false_posibility=predicted[0][0]
    #     false_posibilities.append(false_posibility)
    labels.append(label)
    true_posibilities.append(true_posibility)
for text,label,posibility in zip(texts,labels,true_posibilities):
    print('%s\t%s\t%s'%(label, text,posibility))

df = pd.DataFrame({'sentence':texts, "labels": labels,"true_posibilities":true_posibilities})
df_truePo_sorted = df.sort_values(by="true_posibilities", ascending=False)
df_truePo_sorted=df_truePo_sorted.loc[df_truePo_sorted['true_posibilities']>0.9]
print(df_truePo_sorted)
# df.to_csv('output/result_labels_'+outfile+'.csv',index=False)
df_truePo_sorted.to_csv('output/result_'+outfile+'.csv',index=False)
