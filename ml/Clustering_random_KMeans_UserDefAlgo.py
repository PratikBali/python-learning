import numpy as np
import pandas as pd
from copy import deepcopy
from matplotlib import pyplot as plot


def KMean():
    # Set three centers, the model should predictv similar result
    center_1 = np.array([1, 1])
    print(center_1)

    center_2 = np.array([5, 5])
    print(center_2)

    center_3 = np.array([8, 1])
    print(center_3)

    # generate random data and center it to the three centers
    data_1 = np.random.randn(7, 2)+center_1
    print("\n element of first cluster with size "+str(len(data_1)))
    print(data_1)

    data_2 = np.random.randn(7, 2)+center_2
    print("elements of second cluster with size "+str(len(data_2)))
    print(data_2)

    data_3 = np.random.randn(7, 2)+center_3
    print("element of third cluster with size "+str(len(data_3)))
    print(data_3)

    data = np.concatenate((data_1, data_2, data_3), axis=0)
    print("\n size of complete data set "+str(len(data)))

    plot.scatter(data[:, 0], data[:, 1], s=7)
    plot.title('Marvellous Infosystem : Input Dataset')
    # plot.show()

    # number of clusters
    k = 3

    # number of training data
    n = data.shape[0]
    print("Total number of elements are ", n)

    # number of features in the data
    c = data.shape[1]
    print("Total number of elements are ", n)

    # Generate random centers, here we use sigma and mean to ensure it represent the whole data
    mean = np.mean(data, axis=0)
    print('Value of mean ', mean)

    # Calculate standard deviation
    std = np.std(data, axis=0)
    print('Value of std ', std)

    centers = np.random.randn(k, c)*std + mean
    print('\n Random points are \n', centers)

    # Plot the data and the centeres generated as random
    plot.scatter(data[:, 0], data[:, 1], c='r', s=7)
    plot.scatter(centers[:, 0], centers[:, 1], marker='*', c='g', s=150)
    plot.title('Marvellous Infosystem : Input Dataset with random centroid')
    plot.show()

    # To store old centers
    centers_old = np.zeros(centers.shape)
    print('\n old centroid \n', centers_old)

    # To store new centers
    centers_new = deepcopy(centers)
    print('new centroid \n', centers_new)

    data.shape
    clusters = np.zeros(n)
    distances = np.zeros((n, k))

    print('\n Initial distances are \n', distances)
    error = np.linalg.norm(centers_new - centers_old)

    print('error', error)

    # When, after an update, the estimate of that center stays the same, exit loop
    while error != 0:

        # measure distance to every center
        print('Measure the distance from centroid to every center')
        for i in range(k):
            print('Interation number ', i)
            distances[:, i] = np.linalg.norm(data - centers[i], axis=1)

        # Assign all training data to closest center
        clusters = np.argmin(distances, axis=1)

        centers_old = deepcopy(centers_new)

        # Calculate mean for every cluster and update the center
        for i in range(k):
            centers_new[i] = np.mean(data[clusters == i], axis=0)
        error = np.linalg.norm(centers_new - centers_old)

    # end of while
    centers_new

    # plot the data and the center generated as random
    plot.scatter(data[:, 0], data[:, 1], s=7)
    plot.scatter(centers[:, 0], centers[:, 1], marker='*', c='g', s=150)
    plot.title('Marvellous Infosystem : Final data with centroid')
    plot.show()


def main():
    print(".....Marvellous Infosystem by piyush sir.....")
    print("unsupervised Machine Learning")
    print("clustering using K Mean Algorithm")
    KMean()


if __name__ == "__main__":
    main()
