# implementation of logistic regression
# predicting the output variable from input
# created by sachin mukherjee
# sachinmukherjee29@gmail.com
from math import e


def logisticRegression(inp):
    x1 = inp[0]                                             # x1 from input
    x2 = inp[1]                                             # x2 from input
    b0 = 0                                                  # initialising coficient
    b1 = 0
    b2 = 0
    output = 0                                              # initialising output
    alpha = 0.3                                             # taking alpha as 0.3
    output = b0 + b1 * x1 + b2 * x2
    prediction = 1 / (1 + pow(e, -output))
    for x in range(11):                                     # making 10 iteration for better results
        # cofficient = previous cofficient value + alpha * (output-prediction) * prediction * (1 - prediction) * input value according to cofficient
        b0 = b0 + alpha * (output-prediction) * prediction * (1 - prediction) * 1.0
        b1 = b1 + alpha * (output-prediction) * prediction * (1 - prediction) * x1
        b2 = b2 + alpha * (output-prediction) * prediction * (1 - prediction) * x2
        output = b0 + b1 * x1 + b2 * x2                     # calculating output from cofficients
        prediction = 1 / (1 + pow(e, -output))              # predicting output
    if prediction > 0.5:
        print "Class 1"
    else:
        print "Class 0"

inp = [2.7810836, 2.550537003]
logisticRegression(inp)


