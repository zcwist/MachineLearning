import MPlsa

import time

startTime = time.clock()

k = 12

docs = []
fileHandle = open("Feature.txt")

for lines in fileHandle.readlines():
	docs.append(eval(lines))
fileHandle.close()

fileHandle = open("Corpus.txt")
corpus = eval(fileHandle.read())
fileHandle.close()

# now = time.clock()
# print "spent %fs on import" % (now - startTime)
# startTime = now

for k in range(5):
	plsa = MPlsa.Plsa(docs, corpus, k+22)
	plsa.train(10)
	print "when topics = %d" %(k + 2)
# plsa.printW_z()

# now = time.clock()
# print "spent %fs on algorithm" % (now - startTime)