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

-train(): 训练。两次迭代Likelihood相对误差小于1e-4时，视为收敛。

###2.PreProcessing.py

对原文本进行预处理，产生文档集的稀疏矩阵，生成语料库

###3.main.py

调用中间文间，运行PLSA算法，输出结果。

##算法结果
Likelihood = -456024.296419 when topics = 2

Likelihood = -463233.650388 when topics = 3

Likelihood = -468130.593923 when topics = 4

Likelihood = -471398.605316 when topics = 5

Likelihood = -474394.409650 when topics = 6

Likelihood = -476905.849248 when topics = 7

Likelihood = -479083.955735 when topics = 8

Likelihood = -480845.583321 when topics = 9

Likelihood = -481568.807240 when topics = 10

Likelihood = -483081.719609 when topics = 11

Likelihood = -484087.188684 when topics = 12
 
Likelihood = -483933.304251 when topics = 12

Likelihood = -485505.698568 when topics = 13

Likelihood = -486112.447189 when topics = 14

Likelihood = -486926.796773 when topics = 15

Likelihood = -487488.446365 when topics = 16

Likelihood = -488413.807935 when topics = 17

Likelihood = -489091.446733 when topics = 18

Likelihood = -489842.893020 when topics = 19

Likelihood = -490048.383656 when topics = 20

Likelihood = -490805.864386 when topics = 21

Likelihood = -491580.432400 when topics = 22

Likelihood = -491974.951833 when topics = 23

Likelihood = -492814.541796 when topics = 24

Likelihood = -492937.930725 when topics = 25

Likelihood = -493039.603267 when topics = 26
