# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:00:43 2019

@author: pingj
"""

from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
    #create data
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,labels
    
def classify0(inX,dataSet,labels,k):
    #calculate the distance
    dataSetSize=dataSet.shape[0]
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    
    #sort and find the closest k nodes in traing set
    sortedDistIndicies=distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
        
    #decide the label of node
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    #trans file to matrix
    fr=open(filename)
    arrayOLines=fr.readlines()
    numberOfLines=len(arrayOLines)
    returnMat=zeros((numberOfLines,3))
    classLabelVector=[]
    index=0;
    for line in arrayOLines:
        line=line.strip()
        listFromLine=line.split('\t')
        returnMat[index:]=listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index+=1
    return returnMat,classLabelVector

def show(datingDataMat):
    #show data in picture
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
    plt.show()
    
def autoNorm(dataSet):
    #calculate max and min value in column, calculate ranges of columns
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals
    #prepare the output
    normDataSet=zeros(shape(dataSet))
    m=dataSet.shape[0]
    #normalize the matrix
    normDataSet=dataSet-tile(minVals,(m,1))
    normDataSet=normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals
    
def datingClassTest():
    #set test set range
    hoRatio=0.10
    #get data set from file
    datingDataMat,datingLabels=file2matrix('datingTestSet2.txt')
    #normalize
    normMat,ranges,minVals=autoNorm(datingDataMat)
    m=normMat.shape[0]
    numTestVecs=int(m*hoRatio)
    errorCount=0.0
    #test set range is [0~numTestVect], tring set range is [numTestVect~m]
    for i in range(numTestVecs):
        classifierResult=classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print("The classifier came back with: %d, the real answer is: %d" %(classifierResult,datingLabels[i]))
        if (classifierResult!=datingLabels[i]):
            errorCount+=1.0
    print("The total error rate is: %f" %(errorCount/float(numTestVecs)))
    
def classifyPerson():
    #get input data
    resultList=['not at all','in small doses','in large doses']
    percentTats=float (input('Percentage of time spend playing video games?'))
    ffMiles=float(input('Frequent flier miles earned per year?'))
    iceCream=float(input('Liters of ice cream consumed per year?'))
    #get data set from file
    datingDataMet,datingLabels=file2matrix('datingTestSet2.txt')
    #normalize data set
    normMat,ranges,minVals=autoNorm(datingDataMat)
    #generate input data array and test input
    inArr=array([ffMiles,percentTats,iceCream])
    classifierResult=classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print('You will probably like this person: ',resultList[classifierResult-1])
    