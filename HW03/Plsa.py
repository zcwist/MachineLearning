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
	def __init__(self, docs, wordNum, topics):
		self.docs = docs
		self.wordNum = wordNum
		self.topics = topics
		self.z_dw = {}
		#[[0 for col in range(5)] for row in range(3)]
		self.w_z = [[0 for col in range(topics)] for row in range(wordNum)]
		self.d_z = [[0 for col in range(topics)] for row in range(len(docs))]
		self.z = [0] * topics
		self.sumOfNdw = 0 # sum(n(d,w)) d in D, w in W
		for doc in self.docs:
			d = self.docs.index(doc)
			for word in doc:
					self.z_dw[(d,word)] = randNormVector(self.topics)
					self.sumOfNdw += doc[word]
		self.mStep()

	def eStep(self):
		for doc in self.docs:
			d = self.docs.index(doc)
			for word in doc:
				sum = 0
				for i in range(self.topics):
					sum += self.w_z[word][i] * self.d_z[d][i] * self.z[i]
				for i in range(self.topics):
					self.z_dw = self.w_z[word][i] * self.d_z[d][i] * self.z[i] / sum

	def mStep(self):
		for i in range(self.topics):
			sumOfNdwPzdwForDW = 0 #sum(n(d,w)*P(z|d,w)) d in D, w in W
			for doc in self.docs:
				d = doc.index(doc)
				for word in doc:
					sumOfNdwPzdwForDW += doc[word] * self.z_dw[i]
			
			#calc p(w|z)
			sumOfNdwPzdwForD = 0 #sum(n(d,w)*P(z|d,w)) d in D
			for w in range(self.wordNum):
				for d in self.docs:
					sumOfNdwPzdwForD += d.get(w,0) * self.z_dw[(w,d)][i]
				self.w_z[w][z] = sumOfNdwPzdwForD / sumOfNdwPzdwForDW

			#calc p(d|z)
			sumOfNdwPzdwForW = 0 #sum(n(d,w)*P(z|d,w)) w in W
			for d in self.docs:
				for w in d:
					sumOfNdwPzdwForW += d.get(w,0) * self.z_dw[(w,d)][i]
				self.d_z[d][z] = sumOfNdwPzdwForW / sumOfNdwPzdwForDW

			#calc p(z)
			self.z[i] = sumOfNdwPzdwForDW / self.sumOfNdw

	def calLikelihood(self):
		self.likelihood = 0
		for d in self.docs:
			for w in d:
				sumOfPwzPdzPz = 0
				for i in range(self.topics):
					sumOfPwzPdzPz += self.w_z[w][i] * self.d_z[w][i] * self.z[i]
				self.likelihood += d[w] * math.log(sumOfPwzPdzPz)

	# def train(self, maxIter = 10):
	# 	print maxIter
	# 	cur = 0
 #        for i in range(10):
 #            print '%d iter' % i
 #            self.eStep()
 #            self.mStep()
 #            self.calLikelihood()
 #            print 'likelihood %f ' % self.likelihood
 #            if cur != 0 and abs((self.likelihood-cur)/cur) < 1e-8:
 #                break
 #            cur = self.likelihood



			


