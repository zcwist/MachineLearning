import Plsa

import time

startTime = time.clock()

k = 5

docs = []
fileHandle = open("Feature.txt")

for lines in fileHandle.readlines():
	docs.append(eval(lines))
fileHandle.close()

fileHandle = open("Corpus.txt")
corpus = eval(fileHandle.read())
fileHandle.close()

now = time.clock()
print "spent %f on import" % (now - startTime)
startTime = now

plsa = Plsa.Plsa(docs, corpus, k)
plsa.train(10)
#plsa.printW_z()

now = time.clock()
print "spent %f on algorithm" % (now - startTime)


