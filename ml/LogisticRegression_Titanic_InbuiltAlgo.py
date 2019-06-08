import math
import numpy as np
import pandas as pd  # To read csv
from seaborn import countplot
from matplotlib.pyplot import figure, show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def TrainData(features, target):
    data_train, data_test, target_train, target_test = train_test_split(
        features, target, test_size=0.5)

    model = LogisticRegression()

    model.fit(data_train, target_train)

    # step 4 : Data testing

    predicted = model.predict(data_test)

    print(predicted)

    # Calculate accuracy
    print('Classification report of logistic regression ')
    print(classification_report(target_test, predicted))

    print('Confusion matrix of logistic regression ')
    print(confusion_matrix(target_test, predicted))

    print('Accuracy of logistic regression ')
    print(accuracy_score(target_test, predicted))


def LogisticRegressionUsingTitanic():
    # step 1 : Load data
    titanic_data = pd.read_csv('../datasets/DatasetTitanic.csv')

    print('First 5 entries from loaded dataset')
    print(titanic_data.head())

    print('No. of passengers: '+str(len(titanic_data)))

    # step 2 : Analyze data

    # Total Survived and non survived
    print('Visualization: Total Survived and non survived')
    figure()
    target = 'Survived'
    countplot(data=titanic_data, x=target).set_title(
        'Survived and non survived')
    # show()

    # Survived and non survived based on gender
    print('Visualization: Survived and non survived based on gender')
    figure()
    target = 'Survived'
    countplot(data=titanic_data, x=target, hue='Sex').set_title(
        'Survived and non survived based on gender')
    # show()

    # Survived and non survived based on passenger class
    print('Visualization: Survived and non survived based on passenger class')
    figure()
    target = 'Survived'
    countplot(data=titanic_data, x=target, hue='Pclass').set_title(
        'Survived and non survived based on passenger class')
    # show()

    # Survived and non survived based on Age
    print('Visualization: Survived and non survived based on Age')
    titanic_data['Age'].plot.hist().set_title(
        'Survived and non survived based on Age')
    # show()

    # Survived and non survived based on Fare
    print('Visualization: Survived and non survived based on Fare')
    figure()
    titanic_data['Fare'].plot.hist().set_title(
        'Survived and non survived based on Fare')
    # show()

    # Data cleaning

    print('First 5 entries after removing column zero ')
    titanic_data.drop('zero', axis=1, inplace=True)
    print(titanic_data.head())

    print('Values of Sex column')
    print(pd.get_dummies(titanic_data['Sex'].head()))

    print('Values of Sex column after removing one field')
    new_sex = pd.get_dummies(titanic_data['Sex'], drop_first=True)
    print(new_sex.head())

    print('Values of Pclass column')
    print(pd.get_dummies(titanic_data['Pclass'].head()))

    print('Values of Pclass column after removing one field')
    new_Pclass = pd.get_dummies(titanic_data['Pclass'], drop_first=True)
    print(new_Pclass.head())

    print('Values of Age column')
    print(pd.get_dummies(titanic_data['Age'].head()))

    print('Concatenating new columns')
    new_titanic_data = pd.concat([titanic_data, new_sex, new_Pclass], axis=1)
    print(new_titanic_data.head())

    print("Removing 4 irrelevant columns 'Sex','sibsp', 'Parch', 'Embarked'")
    new_titanic_data.drop(
        ['Sex', 'sibsp', 'Parch', 'Embarked'], axis=1, inplace=True)
    print(new_titanic_data.head())

    # Data training
    x = new_titanic_data.drop('Survived', axis=1)
    y = new_titanic_data['Survived']
    TrainData(x, y)


def main():
    LogisticRegressionUsingTitanic()


if __name__ == "__main__":
    main()
