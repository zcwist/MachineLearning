import os

fileHandle = open("dataDemo.txt")
docNum = fileHandle.readline()

wordList = []

featureFile = open("Feature.txt","w")


for doc in fileHandle.readlines():
	feature = {}
	for word in doc.split():
		if word not in wordList:
			wordList.append(word)
		index = wordList.index(word)
		feature[index] = feature.get(index, 0) + 1
	featureFile.write(str(feature)+"\n")

fileHandle.close()
featureFile.close()

corpus = open ("Corpus.txt","w")
corpus.write(str(wordList))
corpus.close()