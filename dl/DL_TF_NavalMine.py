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
    return (train_test_split(
        X, Y, test_size=0.30, random_state=415))


# STEP 5 # Define variables and placeholders
def make_variables(X, Y):

    # The amount by which weight will be adjusted
    learning_rate = 0.3

    # Number of iteration
    training_epochs = 0.3

    # Array that stores cost value in successive epochs
    cost_history = np.empty(shape=[1], dtype=float)

    # No of features / no of columns
    n_dim = X.shape[1]
    print('dimension:', n_dim)

    # Classes are rock and mine(R & M)
    n_class = 2

    # Numbers of hidden layrs are 4
    # Numbers of nurons per layer are 60
    n_hidden_1 = 60
    n_hidden_2 = 60
    n_hidden_3 = 60
    n_hidden_4 = 60

    # Placeholders to store input
    x = tf.compat.v1.placeholder(tf.float32, [None, n_dim])

    # Placeholders to store output
    y_ = tf.compat.v1.placeholder(tf.float32, [None, n_class])

    # Model parameter
    W = tf.Variable(tf.zeros([n_dim, n_class]))
    B = tf.Variable(tf.zeros([n_class]))

    # Tensor variable for storing weight values
    # creating variable which contains random values
    weights = {
        'h1': tf.Variable(tf.random.truncated_normal([n_dim, n_hidden_1])),
        'h2': tf.Variable(tf.random.truncated_normal([n_hidden_1, n_hidden_2])),
        'h3': tf.Variable(tf.random.truncated_normal([n_hidden_2, n_hidden_3])),
        'h4': tf.Variable(tf.random.truncated_normal([n_hidden_3, n_hidden_4])),
        'out': tf.Variable(tf.random.truncated_normal([n_hidden_4, n_class])),
    }
    print('weights\n', weights)

    # Tensor variable for storing bias values
    # creating variable which contains random values
    bias = {
        'h1': tf.Variable(tf.random.truncated_normal([n_hidden_1])),
        'h2': tf.Variable(tf.random.truncated_normal([n_hidden_2])),
        'h3': tf.Variable(tf.random.truncated_normal([n_hidden_3])),
        'h4': tf.Variable(tf.random.truncated_normal([n_hidden_4])),
        'out': tf.Variable(tf.random.truncated_normal([n_class])),
    }
    print('\nbias\n', bias)

    # Initialization of variable
    init = tf.compat.v1.global_variables_initializer()

    saver = tf.compat.v1.train.Saver()

    # Call to model function for training
    y = multilayer_perceptron(x, weights, bias)


def multilayer_perceptron(x, weights, bias):
    print('hi')


# Entry point function
def main():
    X, Y = read_dataset()
    make_variables(X, Y)
    train_data, test_data, train_target, test_target = split(X, Y)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    exetime = end - start
    print('Execution time', exetime)
