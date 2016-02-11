#coding:utf-8

import numpy as np
import sys
import traceback

# get data from word.csv
f = open("semanticAnalysis/word.csv")
res = f.read()
f.close()
line = res.split("\n")
worditem = []
for i in range(1,len(line)-1):
	worditem.append(line[i].split(","))

# get data from order.csv
f2 = open("semanticAnalysis/order.csv")
res2 = f2.read()
f2.close()
line2 = res2.split("\n")
orderitem = []
for i in range(1,len(line2)-1):
	orderitem.append(line2[i].split(","))

def send(sentence):
	"""
	send() execute semantic-analysis.
	sentence is array of string.
	length is variable.
	"""
	# initialize
	featureVector.fv = np.arange(0)
	# get feature vector
	parseList(sentence)
	# collation between feature vector and model
	if len(featureVector.fv) == 0:
		return -1
	resultModel = featureVector.collation()
	# get ordernumber 
	ordernumber = featureVector.modelDecode(resultModel)
	return ordernumber

def parseList(sentence):
	"""parse array to word, and try to find feature vector."""
	try:
		for word in sentence:
			# get list of vector and weight
			flag, res = searchWord(word)
			for vec in res:
				ary = vec.split(":")
				v = ary[0]
				w = ary[1]
				if flag == True:
					featureVector.setVector(int(v), weight=float(w))
	except:
		print("Exception in parseList.")
		print "--------------------------------------------"
		print traceback.format_exc(sys.exc_info()[2])
		print "--------------------------------------------"

def searchWord(word):
	"""
	judge whether inputword correspond with data on word.csv.
	return flag and res, res=[v1:w1,v2:w2...] or []
	"""
	flag = False
	res = []
	try:
		for buf in worditem:
			if word == unicode(buf[1],"utf-8"):
				print "In semanticAnalysis.py, hitword:%s, buf[0]:%s" % (word, unicode(buf[0],"utf-8"))
				res.append(buf[3])
				flag = True
		return flag, res
	except:
		print "Exception in searchWord."
		print "--------------------------------------------"
		print traceback.format_exc(sys.exc_info()[2])
		print "--------------------------------------------"
		return False, res 

class featureVector:
	fv = np.arange(0)
	model = []

	@classmethod
	def initVector(self):
		"""init feature vector."""
		seq = np.arange(100.)
		mat = seq.reshape((10,10))
		mat *= 0
		return mat
	
	@classmethod
	def setVector(self, coordinate, weight=1, vectype="input"):
		"""set feature vector include init."""
		try:
			# select vector
			if vectype == "input":
				v = featureVector.fv
			elif vectype == "model":
				v = np.arange(0)
			# init vector
			if len(v) == 0:
				v = featureVector.initVector()
			# set value
			column = coordinate % 10
			row = (coordinate - column)/10
			v[row][column] += weight
			# update
			if vectype == "input":
				featureVector.fv = v
			elif vectype == "model":
				featureVector.model.append(v)
		except:
			print "Exception in setVector."
			print "coordinate:%d, weight=%d" % (coordinate, reward)
	
	@classmethod
	def setModel(self):
		"""Set order model to matrix."""
		try:
			for buf in orderitem: # init model
				featureVector.setVector(int(unicode(buf[1],"utf-8")),vectype="model")
		except:
			print("Exception in setModel")

	@classmethod
	def collation(self):
		"""collate model and feature vector."""
		try:
			# init model
			if len(featureVector.model) == 0:
				print "init model"
				featureVector.setModel()
			# search error between model and feature vector
			candidate = featureVector.model[0], 9999 # model, df-value
			for model in featureVector.model:
				df = model - featureVector.fv
				ones = np.repeat(np.array([1]), 10) # (1, 1, 1, ... , 1)
				summation = np.dot(np.abs(df), ones).dot(ones)
				# update candidate
				if summation < candidate[1]:
					candidate = model, summation 
			print candidate
			return candidate[0]
		except:
			print("Exception in collation.")
			print "--------------------------------------------"
			print traceback.format_exc(sys.exc_info()[2])
			print "--------------------------------------------"

	
	@classmethod
	def modelDecode(self,model):
		"""convert model-matrix to Number on order.csv"""
		print("start modeldecode")
		coordinate = np.where(model==1)
		if not len(coordinate[0]) == 1:
			print("unforecasted model.")
			return -1
		number = coordinate[0][0]*10 + coordinate[1][0]
		return number
