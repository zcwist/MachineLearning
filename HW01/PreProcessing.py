# -*- coding: utf-8 -*- 
import tfidf
import os


table = tfidf.Tfidf()

positive = 1
negative = -1

#import files
path = 'data 1/s1/baseball/'
demopath = 'demodata/'
for root, dirs, files in os.walk(path):
	for f in files:
		if f == ".DS_Store" : continue
		fileHandle = open (os.path.join(root,f))
		table.addDocument(positive, f, fileHandle.read().split())
		fileHandle.close()

doclist = table.getTfIdf()
print doclist[0]