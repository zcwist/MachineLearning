# -*- coding: utf-8 -*-
import random
import math

class Plsa:
	def __init__(self, docs, corpus, topics):
		self.docs = docs
		self.corpus = corpus
		self.docNum = len(docs)
		self.wordNum = len(corpus)
		self.topics = topics
		self.z_dw = [] 
		#[[0 for col in range(5)] for row in range(3)]
		self.w_z = [[0 for col in range(self.wordNum)] for row in range(topics)]
		self.d_z = [[0 for col in range(topics)] for row in range(len(docs))]
		self.z = [0] * topics

		self.makeIndex()
		
		#first e-step
		self.sumOfNdw = 0 # sum(n(d,w)) d in D, w in W
		for d in range(self.docNum):
			self.z_dw.append({})
			for w in self.docs[d]:
				self.z_dw[d][w] = [0] * topics
				for z in range(topics):
					self.z_dw[d][w][z] = random.random()
					self.sumOfNdw += self.docs[d][w]
				norm = sum(self.z_dw[d][w])
				for i in range(topics):
					self.z_dw[d][w][i] /= norm
		self.mStep()

	def makeIndex(self):
		self.wordIndex = []
		for w in range(self.wordNum):
			self.wordIndex.append([])
			for doc in self.docs:
				if w in doc:
					self.wordIndex[w].append(self.docs.index(doc))


	def eStep(self):
		#calc P(z|d,w)
		for d in range(self.docNum):
			for w in self.docs[d]:
				sum = 0
				for i in range(self.topics):
					sum += self.w_z[i][w] * self.d_z[d][i] * self.z[i]
				for i in range(self.topics):
					self.z_dw[d][w][i] = self.w_z[i][w] * self.d_z[d][i] * self.z[i] / sum

	def mStep(self):
		for i in range(self.topics):
			sumOfNdwPzdwForDW = 0 #sum(n(d,w)*P(z|d,w)) d in D, w in W
			for d in range(self.docNum):
				for w in self.docs[d]:
					sumOfNdwPzdwForDW += self.docs[d][w] * self.z_dw[d][w][i]
			
			#calc p(w|z)
			for w in range(self.wordNum):
				sumOfNdwPzdwForD = 0 #sum(n(d,w)*P(z|d,w)) d in D
				for d in self.wordIndex[w]:
					sumOfNdwPzdwForD += self.docs[d][w] * self.z_dw[d][w][i]
				self.w_z[i][w] = sumOfNdwPzdwForD / sumOfNdwPzdwForDW

			#calc p(d|z)
			for d in range(self.docNum):
				sumOfNdwPzdwForW = 0 #sum(n(d,w)*P(z|d,w)) w in W
				for w in self.docs[d]:
					sumOfNdwPzdwForW += self.docs[d][w] * self.z_dw[d][w][i]
				self.d_z[d][i] = sumOfNdwPzdwForW / sumOfNdwPzdwForDW

			#calc p(z)
			self.z[i] = sumOfNdwPzdwForDW / self.sumOfNdw
		# for i in range(self.topics):
		# 	print self.w_z[i]

	def calLikelihood(self):
		self.likelihood = 0
		for d in range(self.docNum):
			for w in self.docs[d]:
				sumOfPwzPdzPz = 0
				for i in range(self.topics):
					sumOfPwzPdzPz += self.w_z[i][w]  * self.z[i] * self.d_z[d][i]
				self.likelihood += self.docs[d][w] * math.log(sumOfPwzPdzPz)

	def train(self, maxIter = 20):
		# print maxIter
		cur = 0
		for i in range(maxIter):
			# print '%d iter' % i
			self.eStep()
			self.mStep()
			self.calLikelihood()
			# print 'likelihood %f ' % self.likelihood
			if cur != 0 and abs((self.likelihood-cur)/cur) < 1e-4:
				break
			cur = self.likelihood
		print "iter times = %d" % i
		print "likelihood = %f" % self.likelihood
	
	def printW_z(self, topMax = 10):
		for z in range(self.topics):
			print "-------------------------"
			print "topic %d:" % z
			sortedWordList = []
			wordProp = {}
			for w in range(self.wordNum):
				wordProp[self.corpus[w]] = self.w_z[z][w]
			
			sortedWordList = sorted(wordProp.iteritems(), key=lambda d:d[1], reverse = True)
			sum = 0
			for (word,v) in sortedWordList:
				print "%s:%f" %(word,v)
				sum += 1
				if sum >=  topMax:
					break
			print "-------------------------"