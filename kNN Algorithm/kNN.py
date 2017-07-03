# A python program for kNN algorithm
# created by Sachin Mukherjee
# sachinmukherjee29@gmail.com
from math import sqrt
# training example for an algorithm
training_set = [[3, 104, 'R'], [2, 100, 'R'], [1, 81, 'R'], [101, 10, 'A'], [99, 5, 'A'], [98, 2, 'A']]

# target variable for each training example
labels = ['R', 'R', 'R', 'A', 'A', 'A']


def KNN(test, training_set, k):
    result = []                                 # for storing result of the distance calculation and sorted distances
    knn = []                                    # for storing top k sorted results
    x2 = test[0]                                # assigning value of x2 and y2
    y2 = test[1]
    for x, y, z in training_set:
        x1 = x
        y1 = y
        label = z
        distance = sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))        # distance calculation
        result.append((distance, label))                            # appending each distance to result
    result.sort()                                                   # sorting the distance in acceding order
    for i in range(k):                                              # taking the top k distance from the sorted result
        knn.append(result[i])
    return knn                                                      # returns the top k distances

def classify(knn, training_set):
    classA = 0                                                      # two variable for result
    classB = 0
    labels = []
    for x in range(len(knn)):                                       # to keep all the labels together
        labels.append(knn[x][1])                                    # in label variables
    for y in range(len(labels)):
        if labels[0] == knn[y][1]:                                  # to measure which label class it belogs to
            classA += 1
        else:
            classB += 1
    if classA > classB:
        print "Training Set Belongs to Class A: " + str(classA)
    else:
        print "Training Set Belongs to Class B: " + str(classB)










knn = KNN([18, 90], training_set, 3)
classify(knn, training_set)

