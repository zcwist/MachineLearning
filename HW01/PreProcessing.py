# -*- coding: utf-8 -*- 
import tfidf
import os


table = tfidf.Tfidf()

positive = 1
negative = -1

#import files
path = 'data 1/s1/'
demopath = 'demodata/'
for root, dirs, files in os.walk(demopath):
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

fileHandle = open ('s1FeatureVector.txt', 'w')
for doc in doclist:
	data = "%d" %doc[0] + " " +str(doc[2]) +"\n"
	fileHandle.write(data)
fileHandle.close();
