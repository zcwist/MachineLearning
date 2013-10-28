import sys
import os
import math
from string import punctuation

class Tfidf:
	def __init__(self):
		self.weighted = False
		#documents contains document, and document contains two field: docName and docDict
		self.documents = []

		#corpusDict has all the items from documents
		self.corpusDict = {}

		#tf-idf value of each words in each doc 
		self.tfIdf = []

	# signal: positive doc or negative doc
	def addDocument(self, signal, docName, listOfWords):
		#building a dictionary
		docDict = {}
		for w in listOfWords:

			#delete all punctuations
			w=w.translate(None, punctuation)
			#lowercase
			w=w.lower()

			#count term frequency of a word
			docDict[w] = docDict.get(w, 0.0) + 1.0 

			if (w in self.corpusDict):
				self.corpusDict[w][0] += 1 
				#count number of a word in the doc
				self.corpusDict[w][1] += 1 if (docDict[w] == 1) else 0 #count number of file that contains the word
			else:
				self.corpusDict[w] = [1,1]

		self.documents.append([signal, docName, docDict])

	# count tf-idf
	def countTfIdf(self):
		D = len(self.documents) + 0.0
		for doc in self.documents: # traversal of all documents
			tfIdfDict = {}
			for w in doc[2]: #traversal of words in doc
				tf = doc[2][w] / self.corpusDict[w][0]
				# print D
				# print (1.0 + self.corpusDict[w][1])
				idf = math.log10 (D / (1.0 + self.corpusDict[w][1]))
				ti = tf * idf;
				if (ti > 0.005):
					# tfidfdict[self.corpusdict.keys().index(w)] = ti
					tfIdfDict[w] = ti
			# temp = sorted(tfIdfDict.iteritems(), key=lambda d:d[0])
			self.tfIdf.append([doc[0], doc[1], tfIdfDict])

	#get num of items in corpusDict
	def getCorpusDict(self):
		return self.corpusDict

	def getDocuments(self):
		return self.documents

	def getTfIdf(self):
		self.countTfIdf()
		return self.tfIdf