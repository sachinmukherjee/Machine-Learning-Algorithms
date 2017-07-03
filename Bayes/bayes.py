from numpy import *


def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problem', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'i', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['my', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec


def CreateVocabSet(dataset):
    vocabset = set([])
    for document in dataset:
        vocabset |= set(document)
    return list(vocabset)


def setOfWords2Vec(vocablist, inputset):
    returnVec = [0] * len(vocablist)
    for words in inputset:
        if words in vocablist:
            returnVec[vocablist.index(words)] = 1
        else:
            print "The word is not in my dictionary"
    return returnVec


def trainNBO(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)                     # No of set of 1 and 0 of of word present in dictionary or not
    numWords = len(trainMatrix[0])                      # len of first set of 1 and 0 of words present in dictionary
    pAbusive = sum(trainCategory) / float(numTrainDocs) # probablity of abusive= sum of training class divided by num of training example
    p0Num = zeros(numWords); p1Num = zeros(numWords)
    p0Denom = 0.0; p1Denom = 0.0
    for i in range(numTrainDocs):                       # staring from 0 to 5
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
        print "p1Num" + str(p1Num)
        print p1Denom
    p1Vect = p1Num / p1Denom
    p0Vect = p0Num / p0Denom
    return p0Vect, p1Vect, pAbusive


listOfPost,listClasses = loadDataSet()      # This load the data from pre loaded values
myVocabList = CreateVocabSet(listOfPost)    # Create a set of unique words from training examples
trainMat =[]
for postinDoc in listOfPost:
    trainMat.append(setOfWords2Vec(myVocabList,postinDoc))

p0v,p1v,pAb = trainNBO(trainMat, listClasses)
