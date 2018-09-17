import copy

import pandas as pd
import math
import matplotlib.pyplot as mt
import numpy as np
import sklearn as sk
import sklearn.metrics
from sklearn.linear_model import LogisticRegression
from mnist import MNIST

mndata = MNIST('/home/subhani007/Desktop/ML Assignment/extracted')
mndata.gz = False
images_train, labels_train = mndata.load_training()

images_test, labels_test = mndata.load_testing()
print(len(images_train))
print(len(labels_train))

# for i in range(0, 10):
#     # print(np.array(images_test[i]).reshape(784, 1))
#     # logit.predict(testImages[i],testLabels[i])
#     print('-->', i)
#     print(logit.predict(np.array(images_test[i]).reshape(1, 784)))
#     score = logit.score(np.array(images_test[i]).reshape(1,784), np.array(labels_test[i]).reshape(1,1))
#     print('score:', i, ':', score)


# logitL2 = LogisticRegression(multi_class='ovr', solver='lbfgs',penalty='l1')
# logitL2.fit(images_train, labels_train)
# score = logitL2.score(np.array(images_test).reshape(10000, 784), np.array(labels_test).reshape(10000, 1))
#
# print('predicted accuracy overall:', score)

for i in range(0, 1):
    print('--------------->i:', i)
    print('Class:', i)

    yTrain = copy.deepcopy(labels_train)
    yTest = copy.deepcopy(labels_test)

    # print('=======>yTrain')
    for j in range(0, 60000):
        # print(yTrain[j])
        if (yTrain[j] == i):
            yTrain[j] = 1
            # print('-->if changed:',yTrain[j])
        else:
            yTrain[j] = 0
            # print('-->else changed:', yTrain[j])
    #
    # print('=======>yTest')
    for j in range(0, 10000):
        # print(yTest[j])
        if (yTest[j] == i):
            yTest[j] = 1
        else:
            yTest[j] = 0

    logitL2 = LogisticRegression(penalty='l2', solver='lbfgs')
    logitL2.fit(images_train, yTrain)

    trainScore=logitL2.score(np.array(images_train).reshape(60000, 784), np.array(labels_train).reshape(60000, 1))

    testScore = logitL2.score(np.array(images_test).reshape(10000, 784), np.array(yTest).reshape(10000, 1))
    print('trainScore:',trainScore,'\ntestScore:', testScore)
    print('`````````````````````````````````````````````')
