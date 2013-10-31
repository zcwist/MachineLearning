Perceptron 
==========
Start on Oct 17

##模块说明
###1.Tfidf.py
用于导入样本，计算TF-IDF值
主要方法有：
####
-addDocument(signal, docName, listOfWords):导入文件

	signal:文本所属分类，在此假定baseball 是 positive，hockey 是 negative

	docName:文件名称

	listOfWords:被去除了标点符号的word list

-getTfIdf():获得TfIdf值，返回值是一个List型结果，数据结构[[+/-,docName,{term: TF-IDF-value, ...}]...]