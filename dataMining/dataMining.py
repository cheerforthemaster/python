#coding:utf-8
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(suppress=True)


def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split(',')
        # python3不适用：fltLine = map(float,curLine) 修改为：
        fltLine = list(map(float, curLine))#将每行映射成浮点数，python3返回值改变，所以需要切分数据集为两个子集
        dataMat.append(fltLine)
    tem = []
    realMat=[]
    for j in range(len(dataMat[0])):
        for i in range(len(dataMat)):
            tem.append(dataMat[i][j])
        realMat.append(tem)
        tem=[]

    return realMat

def pca(dataMat, topNfeat=999999):
    meanVals = mean(dataMat, axis=0)
    DataAdjust = dataMat - meanVals #减去平均值
    covMat = cov(DataAdjust, rowvar=0)
    eigVals,eigVects = linalg.eig(mat(covMat)) #计算特征值和特征向量
    print("特征向量：")
    print (eigVects)
    eigValInd = argsort(eigVals)
    print("特征值：")
    eigVals.sort()
    print (eigVals)
    eigValInd = eigValInd[:-(topNfeat+1):-1]   #保留最大的前K个特征值
    redEigVects = eigVects[:,eigValInd]        #对应的特征向量
    lowDDataMat = DataAdjust * redEigVects #将数据转换到低维新空间
    reconMat = (lowDDataMat * redEigVects.T) + meanVals #重构数据
    print("降维后的数据：")
    print(lowDDataMat)
    print("重构后的数据：")
    print(reconMat)
    return lowDDataMat, reconMat

def fig(dataMat,reconMat):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    color=['r','g','b','c','m','y','k','w']
    type=[]
    for i in range(len(reconMat)):
        if reconMat[i][-1] in type:
            continue
        else:
            type.append(reconMat[i][-1])
    print(type)
    for i in range(len(dataMat)):
        col=color[type.index(reconMat[i][-1])]
        ax.scatter(dataMat[i,0],dataMat[i,1],marker='.',s = 90,c = col) #降维数据集
    #ax.scatter(reconMat[:,0].flatten().A[0],reconMat[:,1].flatten().A[0],marker='.',s = 50,c = 'red')#重构后的数据
    plt.show()

'''
if __name__=='__main__':
    dataMat=loadDataSet('123.txt')
    print("原始数据：")
    print(dataMat)
    pca(dataMat)
'''


