# a implementation of decision tree
# a program for predicting outcome for the future input
# created by sachin mukherjee
# sachinmukherjee29@gmail.com


def decisionTree(inp, training_set):
    class_yes = 0                                                   # initialising the count for class yes and class no
    class_no = 0
    coloryes = 0                                                     # initialising the count for input and their respective class
    colorno = 0
    originyes = 0
    originno = 0
    typeyes = 0
    typeno = 0
    color = inp[0]
    origin = inp[1]
    typ = inp[2]

    for x in training_set:                                          # for iterating through the training set
        if x[3] == 'Yes':                                           # for counting number of yes and no
            class_yes += 1
        else:
            class_no += 1

        if x[0] == color and x[3] == 'Yes':
            coloryes += 1
        else:
            colorno += 1
 
        if x[1] == origin and x[3] == 'Yes':
            originyes += 1
        else:
            originno += 1

        if x[2] == typ and x[3] == 'No':
            typeyes += 1
        else:
            typeno += 1
    # probability of red domestic suv
    # probability of red/yes * domestic/yes * suv/yes * probability of yes
    inpyes = coloryes * originyes * typeyes * class_yes
    inpno = colorno * originno * typeno * class_yes
    if inpyes > inpno:
        print "Input belong to class Yes"
    else:
        print "Input belong to class No"


training_set = [['Red', 'Sports', 'Domestic', 'Yes'], ['Red', 'Sports', 'Domestic', 'No'],
                ['Red', 'Sports', 'Domestic', 'Yes'], ['Yellow', 'Sports', 'Domestic', 'No'],
                ['Yellow', 'Sports', 'Imported', 'Yes'], ['Yellow', 'SUV', 'Imported', 'No'],
                ['Yellow', 'SUV', 'Imported', 'Yes'], ['Yellow', 'SUV', 'Domestic', 'No'],
                ['Yellow', 'SUV', 'Imported', 'No'], ['Red', 'Sports', 'Imported', 'Yes']]

inp = ['Red', 'Domestic', 'SUV']
decisionTree(inp, training_set)