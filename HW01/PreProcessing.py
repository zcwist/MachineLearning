# -*- coding: utf-8 -*- 
import Tfidf
import os


table = Tfidf.Tfidf()

positive = 1
negative = -1

#import files
datano = "1"
path = "data 1/s%s/" %datano
multiFile = "data 1/"
evaluationDataNum = 1
demopath = 'demodata/'

for root, dirs, files in os.walk(multiFile):
	for f in files:
		if f == ".DS_Store" : continue
		if ("s%d" %evaluationDataNum) in root: continue
		fileHandle = open (os.path.join(root,f))
		if "baseball" in root:
			table.addDocument(positive, f, fileHandle.read().split())
		else:
			table.addDocument(negative, f, fileHandle.read().split())
		fileHandle.close()

doclist = table.getTfIdf()

fileHandle = open ("midData/FVWithoutNo.%d.txt" %evaluationDataNum, 'w')
#fileHandle = open ("midData/s%sFeatureVector.txt" %datano, 'w')
for doc in doclist:
	data = "%d" %doc[0] + " " +str(doc[2]) +"\n"
	fileHandle.write(data)
fileHandle.close();
