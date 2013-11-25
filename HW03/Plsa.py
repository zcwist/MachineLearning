# -*- coding: utf-8 -*-
import random
import math


def randNormVector(size):
	vec = []
	for _ in range(size):
		vec.append(random.random())
	norm = sum(vec)
	for i in range(size):
		vec[i] /= norm

class Plsa:
	def __init__(self, docs, corpus, topics):
		self.docs = docs
		self.corpus = corpus
		self.wordNum = len(corpus)
		self.topics = topics
		self.z_dw = {}
		#[[0 for col in range(5)] for row in range(3)]
		self.w_z = [{} for row in range(topics)]
		self.d_z = [[0 for col in range(topics)] for row in range(len(docs))]
		self.z = [0] * topics
		
		#first e-step
		self.sumOfNdw = 0 # sum(n(d,w)) d in D, w in W
		for doc in self.docs:
			d = self.docs.index(doc)
			for word in doc:
				self.z_dw[(d, word)] = [0] * topics
				for i in range(topics):
					self.z_dw[(d,word)][i] = random.random()
					self.sumOfNdw += doc[word]
				norm = sum(self.z_dw[(d,word)])
				for i in range(topics):
					self.z_dw[(d,word)][i] /= norm
		self.mStep()


	def eStep(self):
		for doc in self.docs:
			d = self.docs.index(doc)
			for word in doc:
				sum = 0
				for i in range(self.topics):
					sum += self.w_z[i][word] * self.d_z[d][i] * self.z[i]
				for i in range(self.topics):
					self.z_dw[(d,word)][i] = self.w_z[i][word] * self.d_z[d][i] * self.z[i] / sum

	def mStep(self):
		for i in range(self.topics):
			sumOfNdwPzdwForDW = 0 #sum(n(d,w)*P(z|d,w)) d in D, w in W
			for doc in self.docs:
				d = self.docs.index(doc)
				for word in doc:
					sumOfNdwPzdwForDW += doc[word] * self.z_dw[(d,word)][i]
			
			#calc p(w|z)
			for w in range(self.wordNum):
				sumOfNdwPzdwForD = 0 #sum(n(d,w)*P(z|d,w)) d in D
				for doc in self.docs:
					d = self.docs.index(doc)
					if w in doc.keys():
						sumOfNdwPzdwForD += doc[w] * self.z_dw[(d, w)][i]
				self.w_z[i][w] = sumOfNdwPzdwForD / sumOfNdwPzdwForDW
			# print i
			# print self.w_z[i]


			#calc p(d|z)
			for doc in self.docs:
				sumOfNdwPzdwForW = 0 #sum(n(d,w)*P(z|d,w)) w in W
				d = self.docs.index(doc)
				for w in doc:
					sumOfNdwPzdwForW += doc[w] * self.z_dw[(d, w)][i]
				self.d_z[d][i] = sumOfNdwPzdwForW / sumOfNdwPzdwForDW

			#calc p(z)
			self.z[i] = sumOfNdwPzdwForDW / self.sumOfNdw
		# for i in range(self.topics):
		# 	print self.w_z[i]

	def calLikelihood(self):
		self.likelihood = 0
		for doc in self.docs:
			d = self.docs.index(doc)
			for w in doc:
				sumOfPwzPdzPz = 0
				for i in range(self.topics):
					sumOfPwzPdzPz += self.w_z[i][w]  * self.z[i] * self.d_z[d][i]
				self.likelihood += doc[w] * math.log(sumOfPwzPdzPz)

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
		print "iter = %d" % i
		print "likelihood = %f" % self.likelihood
	def printW_z(self, topMax = 10):
		for z in range(self.topics):
			print "-------------------------"
			print "topic %d:" % z
			sortedWordList = []
			sortedWordList = sorted(self.w_z[z].iteritems(), key=lambda d:d[1], reverse = True)
			sum = 0
			for (w,v) in sortedWordList:
				word = self.corpus[w]
				print "%s:%f" %(word,v)
				sum += 1
				if sum >=  topMax:
					break
			print "-------------------------"