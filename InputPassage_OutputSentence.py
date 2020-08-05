import re
infile = input("请输入文档名(txt格式，不需要加后缀)\n")
outfile = infile+'_sentences_division.txt'
cutLineFlag = ["?", "!", ".","..."] #本文使用的终结符，可以修改
sentenceList = []
with open('documents/'+infile+".txt", "r", encoding="UTF-8") as file:
    oneSentence = ""
    for line in file:
        words = line.strip('\r').strip('\n')
        if len(oneSentence)!=0 and oneSentence[-1] == cutLineFlag:
            sentenceList.append(oneSentence.strip() + "\r")
            oneSentence=""
        for word in words:
            if word not in cutLineFlag:
                oneSentence = oneSentence + word
            else:
                oneSentence = oneSentence + word
                if oneSentence.__len__() > 4:
                    sentenceList.append(oneSentence.strip() + "\r")
                oneSentence = ""
with open(outfile, "w", encoding="UTF-8") as resultFile:
    # print(sentenceList.__len__())
    resultFile.writelines(sentenceList)






