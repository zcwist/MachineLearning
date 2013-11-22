import Plsa



k = 1

docs = []
fileHandle = open("Feature.txt")

for lines in fileHandle.readlines():
	docs.append(eval(lines))
fileHandle.close()

fileHandle = open("Corpus.txt")
corpus = eval(fileHandle.read())
fileHandle.close()

wordNum = len(corpus)

plsa = Plsa.Plsa(docs, wordNum, k)
plsa.eStep()

