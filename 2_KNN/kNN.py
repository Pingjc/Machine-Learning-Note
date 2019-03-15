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
    
    
    