# -*- coding: utf-8 -*- 
import tf
import os


table = tf.Tf()

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

# pseudocode of Rosenblatt's algorithm
# for (i = 0; i < D; i ++) {
# 	p = 0;
# 	for (j = 0; j < D(i); j ++) {
# 		p += w[j] * x[j] ;
# 	}
# 	if (y[i] * p <= 0) {
# 		for (j = 0; j < D(i); j ++) {
# 			w[j] += alpha * y[i] * x[j];
# 		}
# 	}
# }
documents = table.getDocuments()
corpus = table.getCorpusDict().keys()

#initialize parameter
w = [0] * len(corpus)
alpha = 0.25

for times in range(1,5):
	for doc in documents:
		p = 0
		x = doc[2]
		for features in corpus:
			p += w[corpus.index(features)] * x.get(features,0.0)
		if (doc[0] * p <= 0):
			for features in corpus:
				w[corpus.index(features)] += alpha * doc[0] * x.get(features,0.0)


print w