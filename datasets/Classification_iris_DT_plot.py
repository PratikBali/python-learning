import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris()

# print(iris)

print('Features')
print(iris.feature_names)

print('Target')
print(iris.target_names)

# indices for removed elements
test_index = [1,51,101]

# Training data with removed elements
train_target = np.delete(iris.target, test_index)
train_data = np.delete(iris.data, test_index, axis=0)

# Testing data for testing on training data
test_target = iris.target[test_index]
test_data = iris.data[test_index]

# from decision tree classifier
classifier = tree.DecisionTreeClassifier()

# Apply training data to form tree
classifier.fit(train_data, train_target)

print('Removed Values')
print(test_target)

print('Result of testing')
print(classifier.predict(test_data))

# Visual plotting

from sklearn.externals.six import StringIO
import pydot

dot_data = StringIO()
tree.export_graphviz(
    classifier,
    out_file=dot_data,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True,
    impurity=False
)

graph = pydot.graph_from_dot_data(dot_data.getvalue())

graph[0].write_pdf('First_Iris_Plot.pdf')
