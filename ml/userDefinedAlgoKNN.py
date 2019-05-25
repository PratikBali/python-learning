from sklearn import tree
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def euc(a,b):
    return distance.euclidean(a,b)

class NewKNN():
    def fit(self, TrainingData, TrainingTarget):
        self.TrainingData = TrainingData
        self.TrainingTarget = TrainingTarget

    def predict(self, TestData):
        predictions = []
        for row in TestData:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self,row):
        bestDistance = euc(row,self.TrainingData[0])
        bestIndex = 0
        for i in range(1,len(self.TrainingData)):
            dist = euc(row,self.TrainingData[i])
            if dist < bestDistance:
                bestDistance = dist
                bestIndex = i
        return self.TrainingTarget[bestIndex]

def KNN():
    border = '-'*50

    iris = load_iris()

    data = iris.data
    target = iris.target

    print(border)
    print('Actual Data Set')
    print(border)

    for i in range(len(target)):
        print('ID: %d, Label: %s, Feature: %s' %(i,iris.data[i],iris.target[i]))
    print('Size of actual data set %d'%(i+1))

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.5)

    print(border)
    print('Training Data Set')
    print(border)

    for i in range(len(data_train)):
        print('ID: %d, Label: %s, Feature: %s' %(i,data_train[i],target_train[i]))
    print('Size of training data set %d'%(i+1))

    print(border)
    print('Test Data Set')
    print(border)

    for i in range(len(data_test)):
        print('ID: %d, Label: %s, Feature: %s' %(i,data_test[i],target_test[i]))
    print('Size of test data set %d'%(i+1))

    print(border)

    classifier = NewKNN()

    classifier.fit(data_train, target_train)

    predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, predictions)

    return Accuracy


def main():
    Accuracy = KNN()
    print('Accuracy using KNN: ', Accuracy*100,'%')

if __name__ == "__main__":
    main()









