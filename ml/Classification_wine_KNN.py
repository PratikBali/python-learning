from sklearn import metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def WinePredictor():
    # Load data
    wine = datasets.load_wine()

    # Features
    print(wine.feature_names)

    # Labels species (class_0, class_1, class_2)
    print(wine.target_names)

    # Wine data top 5 records
    print(wine.data[0:5])

    # Wine Labels (0: class 0, 1: class_1 , 2: class_2)
    print(wine.target)

    # Split data
    data_train, data_test, target_train, target_test = train_test_split(
        wine.data, wine.target, test_size=0.3)  # 70% training and 30% test

    # Create KNN classifier
    knn = KNeighborsClassifier(n_neighbors=3)

    # Train the model using training sets (features, labels)
    knn.fit(data_train, target_train)

    # Predict response from test dataset
    data_predicted = knn.predict(data_test)

    # Calculate the Accuracy
    print('Accuracy:', metrics.accuracy_score(data_predicted, target_test))


def main():
    print('Machine Learning / Superwised / Classification / Wine Predictor')
    WinePredictor()


if __name__ == "__main__":
    main()
