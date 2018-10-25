import copy
import sklearn.linear_model
import sklearn.metrics
import sklearn.model_selection
import matplotlib.pyplot as mt
import numpy as np
from sklearn import svm
import h5py
import sklearn.svm
from sklearn.metrics import f1_score, accuracy_score

from mlxtend.plotting import plot_decision_regions

data1 = h5py.File('/maccuracy_scorent/Education/Sem1/ML/Assignments/Assignment_2/hw-2_20119/data_1.h5', 'r+')
data2 = h5py.File('/mnt/Education/Sem1/ML/Assignments/Assignment_2/hw-2_20119/data_2.h5', 'r+')
data3 = h5py.File('/mnt/Education/Sem1/ML/Assignments/Assignment_2/hw-2_20119/data_3.h5', 'r+')
data4 = h5py.File('/mnt/Education/Sem1/ML/Assignments/Assignment_2/hw-2_20119/data_4.h5', 'r+')


def polynomialKernel(x, y):
    c = 1
    d = 2

    t = np.transpose(y)
    prod = np.dot(x, t)
    # c = np.ones([prod.shape[0], prod.shape[1]], dtype=int)
    sum = c + prod
    p = (sum) ** d

    return p


def polynomialKernel_2(x, y):
    c = 1
    d = 3
    t = np.transpose(y)
    prod = np.dot(x, t)
    # c = np.ones([prod.shape[0], prod.shape[1]], dtype=int)
    sum = c + prod
    p = (sum) ** d

    return p


# ------------------------------------------------------------------------------------------------------


# print(list(data1.keys()))
data1_X = data1['x']
data1_Y = data1['y']

data1X_Values = np.array(data1_X.value)
data1Y_Values = np.array(data1_Y.value)
# print(data1X_Values.shape)
# print(data1Y_Values.shape)

model1 = svm.SVC(kernel=polynomialKernel)

model1.fit(data1X_Values, data1Y_Values)

# print(model1)

out1 = model1.predict(data1X_Values)

print('intercept:', model1.intercept_)
# for i in range(0, 100):
#     print(data1Y_Values[i], '-->', out1[i])

print('Accuracy for model1:', accuracy_score(data1Y_Values, out1))
print('f1 score for model1:', f1_score(data1Y_Values, out1))

X = np.array(data1X_Values)
Y = np.array(data1Y_Values)

X0, X1 = X[:, 0], X[:, 1]

mt.figure('data_1 decision boundary')
mt.scatter(X0, X1, c=Y)
mt.title('Decision boundary')
plot_decision_regions(X, Y, model1, legend=2)
mt.xlabel('x1')
mt.xlabel('x2')
mt.show()
print('-------------------------------------------')

print(list(data2.keys()))
data2_X = data2['x']
data2_Y = data2['y']

data2X_Values = np.array(data2_X.value)
data2Y_Values = np.array(data2_Y.value)

# print(data2X_Values.shape)
# print(data2Y_Values.shape)

model2 = svm.SVC(kernel=polynomialKernel_2)

model2.fit(data2X_Values, data2Y_Values)

# print(model2)

out2 = model2.predict(data2X_Values)

print('intercept 2:', model2.intercept_)
# for i in range(0, 100):
#     print(data2Y_Values[i], '-->', out2[i])
print('Accuracy for model2:', accuracy_score(data2Y_Values, out2))
print('f1 for model2:', f1_score(data2Y_Values, out2))

X = np.array(data2X_Values)
Y = np.array(data2Y_Values)

X0, X1 = X[:, 0], X[:, 1]
mt.figure('data_2 decision boundary')
mt.title('Decision boundary')
mt.scatter(X0, X1, c=Y)
plot_decision_regions(X, Y, model2, legend=2)
mt.xlabel('x1')
mt.xlabel('x2')

mt.show()
print('-------------------------------------------')
#
# print(list(data3.keys()))
data3_X = data3['x']
data3_Y = data3['y']

data3X_Values = np.array(data3_X.value)
data3Y_Values = np.array(data3_Y.value)

# print(data3X_Values.shape)
# print(data3Y_Values.shape)

model3 = svm.LinearSVC(multi_class='ovr')

model3.fit(data3X_Values, data3Y_Values)

# print(model3)

out3 = model3.predict(data3X_Values)

print('intercept 3:', model3.intercept_)
# for i in range(0, 100):
#     print(data3Y_Values[i], '-->', out3[i])
print('Accuracy for model3:', accuracy_score(data3Y_Values, out3))
print('f1 for model3:\n', sklearn.metrics.classification_report(data3Y_Values, out3))
#
X = np.array(data3X_Values)
Y = np.array(data3Y_Values)

X0, X1 = X[:, 0], X[:, 1]
mt.figure('data_3 decision boundary')
mt.title('Decision boundary')
mt.scatter(X0, X1, c=Y)
plot_decision_regions(X, Y, model3, legend=2)
mt.xlabel('x1')
mt.xlabel('x2')
mt.show()

print('-------------------------------------------')

# print(list(data4.keys()))
data4_X = data4['x']
data4_Y = data4['y']

data4X_Values = np.array(data4_X.value)
data4Y_Values = np.array(data4_Y.value)

model4 = svm.SVC(kernel=polynomialKernel)

model4.fit(data4X_Values, data4Y_Values)

# print(model4)

out4 = model4.predict(data4X_Values)

print('intercept 4:', model4.intercept_)
# for i in range(0, len(data4X_Values)):
#     print(data4Y_Values[i], '-->', out4[i])
print('Accuracy for model4:', accuracy_score(data4Y_Values, out4))
print('f1 for model4:', f1_score(data4Y_Values, out4))
#
X = np.array(data4X_Values)
Y = np.array(data4Y_Values)

X0, X1 = X[:, 0], X[:, 1]

mt.figure('data_4 decision boundary')
mt.scatter(X0, X1, c=Y)
mt.title('Decision boundary')
mt.xlabel('x1')
mt.xlabel('x2')
plot_decision_regions(X, Y, model4, legend=2)

print('-------------------------------------------')

mt.show()
