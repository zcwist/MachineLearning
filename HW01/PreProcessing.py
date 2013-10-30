# -*- coding: utf-8 -*- 
import tfidf
import os


table = tfidf.Tfidf()

positive = 5
negative = -1

#import files
datano = "1"
path = "data 1/s%s/" %datano
multifile = "training data/"
demopath = 'demodata/'

for root, dirs, files in os.walk(path):
	for f in files:
		if f == ".DS_Store" : continue
		fileHandle = open (os.path.join(root,f))
		if "baseball" in root:
			table.addDocument(positive, f, fileHandle.read().split())
		else:
			table.addDocument(negative, f, fileHandle.read().split())
		fileHandle.close()

doclist = table.getTfIdf()
# dic= sorted(doclist[9][2].iteritems(), key=lambda d:d[1], reverse = True)
# print dic
# print len(dic)
# print len(table.getCorpusDict())
# print doclist[0][2]

fileHandle = open ("s%sFeatureVector.txt" %datano, 'w')
for doc in doclist:
	data = "%d" %doc[0] + " " +str(doc[2]) +"\n"
	fileHandle.write(data)
fileHandle.close();
