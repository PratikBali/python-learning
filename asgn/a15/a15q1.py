import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.metrics import accuracy_score
from sklearn import tree


def myPredict():
    csv_file = ('WinePredictor.csv')
    data = pd.read_csv(csv_file)
    print(data.head())
    features = data.drop("Class", axis=1)
    print(features.head())
    target = data["Class"]
    print(target.head())

    data_train, data_test, target_train, target_test = train_test_split(
        features, target, test_size=0.5)

    classifier = KNN()

    classifier.fit(data_train, target_train)

    predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, predictions)

    print('Accuracy using KNN: ', Accuracy*100, '%')

    classifier2 = tree.DecisionTreeClassifier()

    classifier2.fit(data_train, target_train)

    predictions2 = classifier2.predict(data_test)

    Accuracy2 = accuracy_score(target_test, predictions2)

    print('Accuracy using DT: ', Accuracy2*100, '%')


def main():
    csv_file = ('WinePredictor.csv')
    excel_file = ('WinePredictor.xlsx')
    data = pd.read_excel(excel_file)
    # print(data.iloc[0:0, ])
    print(data.head())

    features = data.drop("Table 1", axis=1)
    features = features.drop([0], axis=0)
    print(features.head())

    target = data["Table 1"]
    target = target.drop([0], axis=0)
    print(target.head(60))
    print(target.tail(70))

    data_train, data_test, target_train, target_test = train_test_split(
        features, target, test_size=0.5)

    classifier = tree.DecisionTreeClassifier()

    classifier.fit(data_train, target_train)

    predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, predictions)

    print('Accuracy using DT: ', Accuracy*100, '%')


if __name__ == "__main__":
    # main()
    myPredict()
