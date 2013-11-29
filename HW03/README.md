PLSI Implemention
==========
机械系 张承巍 20133102106

##模块说明
###1.MPLSA
用于PLSA算法的实现

主要方法有：

-__init__(docs, corpus, topics):构造函数

docs:文档集，采用List存储Dictionary，存储稀疏矩阵

corpus:语料库，存储所有的单词表，主要用于最后结果输出

topics:主题数

初始化过程中，随机生成规一化的P(z|d,w),进行第一步E步，然后进行M步。

-makeIndex():构造倒排索引

若遍历单词时，再遍历文本，时间成本很大，采用倒排索引，大大提高效率。

-eStep()：EM算法的E-STEP

-mStep(): EM算法的M-STEP

-train(): 训练。两次迭代Likelihood**相对误差小于1e-4**时，视为收敛。

###2.PreProcessing.py

对原文本进行预处理，产生文档集的稀疏矩阵，生成语料库

###3.main.py

调用中间文间，运行PLSA算法，输出结果。

##操作步骤

###1.预处理

	运行PreProcessing.py 进行前处理。可以通过改变topX，改变预处理的行数，大于总行数，则处理所以行。

###2.训练并输出
	
	改变分类数topics，运行main.py 进行训练，并输出分类结果。

##算法结果

分别以分类数为2、3、5为例

###topics = 2

	spent 0.151679s on importing file
	iter times = 22
	likelihood = -454551.971408
	-------------------------
	topic 0:
	web:0.024722
	semantic:0.014825
	data:0.012913
	information:0.011012
	support:0.010910
	knowledge:0.009691
	learning:0.008851
	approach:0.008739
	vector:0.007845
	classification:0.007484
	-------------------------
	-------------------------
	topic 1:
	learning:0.033945
	systems:0.011182
	planning:0.010127
	logic:0.007961
	information:0.007730
	reasoning:0.007477
	model:0.007213
	agents:0.007199
	knowledge:0.007056
	data:0.006972
	-------------------------
	spent 10.435883s on algorithm
	[Finished in 10.7s]

分类解释：

-topic 0:语义网

-topic 1:机器学习

###topics = 3

	spent 0.140538s on importing file
	iter times = 28
	likelihood = -460331.539582
	-------------------------
	topic 0:
	learning:0.031034
	support:0.016292
	systems:0.013215
	classification:0.011959
	vector:0.011954
	networks:0.011668
	data:0.009361
	bayesian:0.009346
	multi-agent:0.009153
	approach:0.008402
	-------------------------
	-------------------------
	topic 1:
	learning:0.030496
	data:0.013964
	planning:0.012966
	search:0.011529
	information:0.011069
	selection:0.010855
	web:0.010801
	feature:0.009650
	decision:0.008272
	based:0.007440
	-------------------------
	-------------------------
	topic 2:
	web:0.030849
	knowledge:0.023412
	semantic:0.020417
	reasoning:0.014108
	logic:0.011368
	information:0.010255
	ontology:0.009541
	approach:0.008848
	extraction:0.008796
	programming:0.008621
	-------------------------
	spent 14.539366s on algorithm
	[Finished in 14.7s]

分类解释：

-topic 0:学习系统

-topic 1:信息获取

-topic 2:语义网

###topics = 5

	spent 0.144273s on importing file
	iter times = 32
	likelihood = -467529.845755
	-------------------------
	topic 0:
	web:0.042768
	semantic:0.020797
	ontology:0.016438
	systems:0.016348
	knowledge:0.015674
	agent:0.014912
	analysis:0.013815
	ontologies:0.012599
	applications:0.012427
	model:0.011521
	-------------------------
	-------------------------
	topic 1:
	learning:0.020900
	text:0.019279
	agents:0.015186
	networks:0.014300
	planning:0.012251
	classification:0.012191
	intelligent:0.010968
	environments:0.010441
	mobile:0.010264
	bayesian:0.009939
	-------------------------
	-------------------------
	topic 2:
	learning:0.036866
	support:0.028806
	logic:0.021087
	vector:0.020710
	language:0.020522
	programming:0.016003
	machine:0.015813
	user:0.013175
	modeling:0.012614
	machines:0.012238
	-------------------------
	-------------------------
	topic 3:
	learning:0.029182
	data:0.028981
	web:0.026687
	selection:0.018392
	extraction:0.017149
	information:0.016766
	classification:0.014099
	feature:0.014081
	mining:0.013805
	search:0.012353
	-------------------------
	-------------------------
	topic 4:
	planning:0.024653
	learning:0.020392
	approach:0.020011
	systems:0.019629
	knowledge:0.018474
	multi-agent:0.015807
	system:0.014063
	data:0.012685
	reasoning:0.012611
	information:0.011110
	-------------------------
	spent 21.982122s on algorithm
	[Finished in 22.2s]

随着分类数目的增多，对分类进行解释变得更加复杂，对这个领域不是太了解，就不能再做细分了。所以最大的分类数选择了5，在调试阶段也尝试过30类以上的分类操作。

##特色

-倒排索引

-list嵌套dictionary，存储稀疏矩阵

-尽可能用list，提高处理效率

##一些体会

以前以为空洞的概念论，现在发挥了大作用。不算特别复杂的公式推导，就能实现这样看起来复杂的功能。

算法的实现，倒不是很麻烦，但是优化就显得很难。

但是在一开始，仅选择100条记录作为sample，分5类，迭代9次，就花了6.8s，跑真实数据的10000多条数据的时候，我直接以为死机了。

后来增加了**倒排索引**的结构，在外层遍历词表的时候，内层不遍历所有文档，而只遍历包含该词的文档，这样一来，文档-词索引，词-文档索引来存储大型的稀疏矩阵，大大提高了效率。此时处理1000组数据，分5类，用时3.9s，但是在处理所有数据的时候，还是耗时433.16s。而这只是进行一种分类方式，这样的时间还是不可接受的。

下面我又进行了优化，可能是python内部的机制决定，对于dictionary的检索速度还是慢。我尽可能地使用list数据结构，又大幅度地减少了时间，对所有文档分5类，耗时22.2s。这样的速度就比较能接受了。

越是想缩短时间，就越是觉得自己基础知识的薄弱，但是不断优化的过程，优化的是程序，提高的是自己的能力。外系生做这个作业，难度是有的，但收获是更大的。

最后，感谢助教不厌其烦的耐心解答。

##

