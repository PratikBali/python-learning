import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as KNN


def myPredict(weather, temparature, play):
    wine = datasets.load_wine()


def main():
    csv_file = ('WinePredictor.csv')
    excel_file = ('WinePredictor.xlsx')
    data = pd.read_excel(excel_file)
    # print(data.iloc[0:0, ])

    features = data.drop("Table 1", axis=1)
    features = features.drop([0], axis=0)
    print(features)

    target = data["Table 1"]
    target = target.drop([0], axis=0)

    data_train, data_test, target_train, target_test = train_test_split(
        features, target, test_size=0.5)

    classifier = KNN()

    classifier.fit(data_train, target_train)

    predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, predictions)

    print('Accuracy using DT: ', Accuracy*100, '%')


if __name__ == "__main__":
    main()
