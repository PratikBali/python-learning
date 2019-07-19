# STEP 1
# Import required libraries
import time
import numpy as np  # functions for preprocessing data
import pandas as pd  # functions for preprocessing data
import tensorflow as tf  # functions for deep learning model
import matplotlib.pyplot as plot  # functions from plotting graph
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# variables
train_data = any
test_data = any
train_target = any
test_target = any


# STEP 2 # Read and encode dataset
def read_dataset():
    df = pd.read_csv('../datasets/DatasetSonar.csv')
    # print(df.head())
    # print(df.columns)
    # print(len(df.columns))

    # Features of dataset
    X = df[df.columns[0:60]].values

    # Label of dataset
    y = df[df.columns[60]]

    # Encode the dependant variable
    encoder = LabelEncoder()

    # Encode character labels into integer 1 or 0 (one hot module)
    encoder.fit(y)
    y = encoder.transform(y)

    # Y = OneHotEncoder(y)
    Y = custom_one_hot_encoder(y)
    print(X.shape)

    return X, Y


# STEP 3 # one hot encode
def custom_one_hot_encoder(labels):
    n_labels = len(labels)
    n_unique_labels = len(np.unique(labels))
    one_hot_encode = np.zeros((n_labels, n_unique_labels))
    one_hot_encode[np.arange(n_labels), labels] = 1
    return one_hot_encode

# STEP 4 # Dividing dataset into training and testing subset


def split(X, Y):
    train_data, test_data, train_target, test_target = train_test_split(
        X, Y, test_size=0.30, random_state=415)


def main():
    features, labels = read_dataset()
    split()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    exetime = end - start
    print('Execution time', exetime)
