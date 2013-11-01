Perceptron 
==========
机械系 张承巍 20133102106

##模块说明
###1.Tfidf.py

用于计算TF-IDF值

主要方法有：
####
-addDocument(signal, docName, listOfWords):导入文件

	signal:文本所属分类，在此假定baseball 是 positive，hockey 是 negative

	docName:文件名称

	listOfWords:被去除了标点符号的word list

-countTfIdf():计算在添加进的文档集合中的各文档中每个词的TF-IDF值，经过实验发现低地0.005的词都是"is" "a"等类似stop words的词，故将其排除

-getTfIdf():获得TfIdf值，返回值是一个List型结果，数据结构[[+/-,docName,{term: TF-IDF-value, ...}]...]

###2.PreProcesing.py

用于对文档进行前处理，导入文档，并对其进行TF-IDF的计算，生成每个文本的向量表达文本，格式为 +/- {"term":value, ...}，这样表示可以较高较地存储”文档-词“这个很稀疏的矩阵,因为我这个处理只进行一次，就采用了手工修改参数的方法

###3.Learning.py

用于通过学习样本进行学习

####
-learnWithOut(num):学习过程采用交叉验证的方法，参数num是验证样本编号，其他文本作为学习样本。经过调试，设置alpha = 1，权值初始值 = 1，具有较好的性能。通过Rosenblatt's algorithm， 计算出学习样本中每个词的value，同样采用Dictionary形式存储，格式为{"terms":weight, ...}，收敛条件为迭代次数大于10或在样本内验证Value无误。迭代结束后，遍历一次，将value = 0的去除，因为在验证过程中:
	
	for feature in vector:
		p += w.get(feature, 0.0) * vector[feature]

计算点积，所有value = 0 的项都不会起作用，在此删除，可以有效减小W向量的规模。

最后输出w向量。

###4.Evaluation.py

用于验证检验样本的结果

####
-evaluate(num): 以编号为num的样本作为验证样本，通过上一步中学习到的W向量，对这个样本进行验证，输出Precision, Recall, F1 Score。

###5.main.py

依次以5个样本中的1个作为验证样本，以其他的作为学习样本，验证算法性能。

##算法结果

依次以1到5号样本作为验证样本，以其他的样本作为学习样本，得到如下结果:

	Learning without: No.1 Data
	Err numbers:0 Iteration Times:2
	Aplly to No.%d Data
	Result:
	precision = 0.909091
	recall = 0.804020
	f1 score = 0.853333
	------------------
	Learning without: No.2 Data
	Err numbers:0 Iteration Times:4
	Aplly to No.%d Data
	Result:
	precision = 0.982558
	recall = 0.849246
	f1 score = 0.911051
	------------------
	Learning without: No.3 Data
	Err numbers:0 Iteration Times:4
	Aplly to No.%d Data
	Result:
	precision = 0.976190
	recall = 0.824121
	f1 score = 0.893733
	------------------
	Learning without: No.4 Data
	Err numbers:0 Iteration Times:4
	Aplly to No.%d Data
	Result:
	precision = 0.977143
	recall = 0.859296
	f1 score = 0.914439
	------------------
	Learning without: No.5 Data
	Err numbers:0 Iteration Times:4
	Aplly to No.%d Data
	Result:
	precision = 0.961111
	recall = 0.873737
	f1 score = 0.915344
	------------------
	[Finished in 7.1s]

各项指标平均值：

	precision = 0.961219
	
	recall = 0.842084

	f1 score = 0.89758

##一些问题：

###1..TF-IDF

TF-IDF统计不仅依赖于单个文档，还依赖于文档所在的集合，所以定义文档集合的不同，会一定程度地影响TF-IDF值。这也带来一个问题，在算法最终应用时，必须对一个文档集进行test，也就是说，给算法一个文档集合，算法区分出其中哪些是属于Baseball，哪些是属于Hockey。 而算法并不能对单个文本进行判断，实用性较差。

###2.算法Recall值较低。

从以上结果可以看出，算法的Precision值较高，可以达到0.95以上，但是Recall较低，直接拉低了F1 score，目前还没有找到问题所在和解决方案。

