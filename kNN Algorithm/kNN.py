# A python program for kNN algorithm
# created by Sachin Mukherjee
# sachinmukherjee29@gmail.com
from math import sqrt
# training example for an algorithm
training_set = ([3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2])

# target variable for each training example
labels = ['R', 'R', 'R', 'A', 'A', 'A']


def KNN(index, training_set, labels, k):
    result = []                                # to store distance
    result_set = ([])                          # to store distance with labels
    top = ([])                                 # to store top k result nearest distance
    x2 = index[0]                              # value for which target value to be found
    y2 = index[1]
    for x, y in training_set:
        x1 = x                                 # to get each set of value from target example
        y1 = y
        distance = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))          # calculating distance
        result.append(distance)                # add each distance to result
        # result.sort(reverse=True)
    n = 0
    while n != len(result):                     # to keep each distance with its associated label
        result_set.append([result[n], labels[n]])
        n += 1
    result_set.sort(reverse=True)               # sor the result in descending order so that we can get less distance
    for i in (0, 1, 2):
        key = min(result_set[i])
        top.append(key)
        i += 1
    print top


KNN([18, 90], training_set, labels, 3)
