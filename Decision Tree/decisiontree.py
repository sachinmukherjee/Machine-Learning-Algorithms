# a program for implementing decision tree
# created by sachin mukherjee
# sachinmukherjee29@gmail.com

from math import log

dataset =  [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
numentries = len(dataset)
labelcount={}
for featVect in dataset:
    currentlabel = featVect[-1]
    if currentlabel not in labelcount.keys():
        labelcount[currentlabel]=0
        labelcount[currentlabel]+=1
    else:
        labelcount[currentlabel]+=1

shannonEnt = 0.0

for key in labelcount:
    prob = float(labelcount[key])/numentries
    shannonEnt+=prob*log(prob,2)
shannonEnt = - shannonEnt

print shannonEnt

