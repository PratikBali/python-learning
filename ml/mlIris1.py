from sklearn.datasets import load_iris

iris = load_iris()

print('Features')
print(iris.feature_names)

print('Target')
print(iris.target_names)

print('First 10')

for i in range(len(iris.target)):
    print('ID: %d, Label: %s, Feature: %s' %(i,iris.data[i],iris.target[i]))