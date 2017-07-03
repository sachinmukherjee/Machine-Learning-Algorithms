# a program for implementing decision tree
# created by sachin mukherjee
# sachinmukherjee29@gmail.com

from math import log


def calShannonENTP(dataset):
    numentries = len(dataset)
    labelcount = {}
    for featVect in dataset:
        currentlabel = featVect[-1]
        if currentlabel not in labelcount.keys():
            labelcount[currentlabel] = 0
            labelcount[currentlabel] += 1
        else:
            labelcount[currentlabel] += 1
    shannonEnt = 0.0
    for key in labelcount:
        prob = float(labelcount[key]) / numentries
        shannonEnt += prob * log(prob, 2)
        shannonEnt = - shannonEnt
    return shannonEnt


def splitData(dataset, axis, value):
    relDataSet = []
    for featVec in dataset:
        if featVec[axis] == value:
            reducedFeatVec = []
            reducedFeatVec.extend(featVec[axis + 1:])
            relDataSet.append(reducedFeatVec)
    return relDataSet


def chooseBestFeature(dataset):
    numFeature = len(dataset[0])-1
    baseEntropy = calShannonENTP(dataset)
    baseInfoGain = 0.0
    baseFeature = -1
    for i in range(numFeature):
        featvec = [example[i] for example in dataset]
        uniqueVals = set(featvec)
        for value in uniqueVals:
            subData = splitData(dataset, i, value)
            prob = len(subData)/float(len(dataset))
            newEntropy =+ prob * calShannonENTP(subData)
        infoGain = baseEntropy-newEntropy
        if(infoGain>baseEntropy):
            baseEntropy=infoGain
            bestFeature = I
    return bestFeature








dataset = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
print splitData(dataset, 1, 0)
chooseBestFeature(dataset)
