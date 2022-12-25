#!/usr/bin/python3

import numpy as np
import operator
import sys
import os
from pathlib import Path


def createDataSet(filePath):

	files = []
	#file_list = os.listdir(filePath)
	#file_list_txt = [file for file in file_list if file.endswith(".txt")]
	#print(file_list_txt)
	for file in Path(filePath).iterdir():
		files.append(str(file))
		
	labels = []
	for i in files:
		tmp = i.split('/')
		labelName = tmp[1][0]
		labels.append(labelName)
		
	data = []
	leng = len(files)
	for j in range(0, leng):
		group = []
		file = open(files[j], "r")
		base = file.read()
		for k in base:
			if (k != '\n'):
				group.append(int(k))
		data.append(group)
			
	dataSet = np.array(data)
	
	file.close()
	return dataSet, labels
	
	

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort() 
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True) 
	return sortedClassCount[0][0] 



#trainingDigits = sys.argv[1]
#testDigits = sys.argv[2]
#t = os.listdir(testDigits)

pathfrom = str(sys.argv[1])
pathto = str(sys.argv[2])
data, label = createDataSet(pathfrom)

for num in range(1, 21):
	cnt = 0
	length = 0
	files = []
	#checkList = os.listdir(p)
	#checkList_txt = [fi for fi in checkList]
	
	
	for file in Path(pathto).iterdir():
		length += 1
		fn = str(file).split('_')
		checkLabel = fn[0][-1]
		#print(checkLabel)
		
		f = open(file, "r")
		base = f.read()
		g = []
		for l in base:
			if (l != '\n'):
				g.append(int(l))
		inX = np.array(g)
			
		value = classify0(inX, data, label, num)
		
		if (checkLabel != value):
			cnt += 1
		
	error = (cnt / length) * 100
	print(int(error))

 
