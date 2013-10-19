import sys
import os
from string import punctuation

class Tf:
	def __init__(self):
		self.weighted = False
		#documents contains document, and document contains two field: docName and doc_dict
		self.documents = []

		#corpusDict has all the items from documents
		self.corpusDict = {}

	def addDocument(self, signal, docName, listOfWords):
		#building a dictionary
		doc_dict = {}
		for w in listOfWords:

			#delete all punctuations
			w=w.translate(None, punctuation)

			#lowercase
			w=w.lower()

			doc_dict[w] = doc_dict.get(w, 0.0) + 1.0
			self.corpusDict[w] = self.corpusDict.get(w, 0.0) + 1.0

		#normalizing the dictionary
		length = float(len(listOfWords))
		for k in doc_dict:
			doc_dict[k] = doc_dict[k] / length

		#add the normalized document to the corpus
		self.documents.append([signal, docName, doc_dict])

	#it seems that this def is useless
	def similarities(self, listOfWords):
		"""Returns a list of all the [docname, similarity_score] pairs relative to a list of words."""

		#building th query dictionary
		queryDict = {}
		for w in listOfWords:
			queryDict[w] = queryDict.get(w, 0.0) + 1.0

		#normalizing the query
		length = float(len(listOfWords))
		for k in queryDict:
			queryDict[k] = queryDict[k] / length

		#computing the list of similaritis
		sims = []
		for doc in self.documents:
			score = 0.0
			doc_dict = doc[1]
			for k in queryDict:
				if doc_dict.has_key(k):
					score += (queryDict[k] / self.corpusDict[k]) + (doc_dict[k] / self.corpusDict[k])
			sims.append([doc[0], score])
		return sims	

	#get num of items in corpusDict
	def getCorpusDict(self):
		return self.corpusDict

	def getDocuments(self):
		return self.documents