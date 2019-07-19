import numpy as np
import pandas as pd
from copy import deepcopy
import matplotlib.pyplot as plot


def HeadBrainPredictor():

    # load data
    data = pd.read_csv('DatasetHeadBrain.csv')

    # print size of data
    print('Size of data:', data.shape)

    # get Data
    axis_x = data['Head Size(cm^3)'].values
    axis_y = data['Brain Weight(grams)'].values

    # Least Square Method
    mean_x = np.mean(axis_x)
    mean_y = np.mean(axis_y)

    n = len(axis_x)

    numerator = 0
    denomenator = 0

    # Equation of line is : y = mx + c

    for i in range(n):

        numerator = numerator + (axis_x[i] - mean_x) * (axis_y[i] - mean_y)

        denomenator = denomenator + (axis_x[i] - mean_x) ** 2

    m = numerator / denomenator

    # Calculate c = y' = mx'

    c = mean_y - (m * mean_x)

    print('Slope of regression line: ', m)
    print('Y intercept of regression line: ', c)

    max_x = np.max(axis_x) + 100
    min_x = np.min(axis_x) - 100

    # plotting
    x = np.linspace(min_x, max_x, n)

    y = m * x + c

    plot.plot(x, y, color='#58b970', label='Regression Line')
    plot.scatter(axis_x, axis_y, color='#ef5423', label='scatter plot')

    plot.xlabel('Head size in cm')
    plot.ylabel('Brain Weight in grams')

    plot.legend()
    plot.show()

    # Find out goodness of fit i.i., R square
    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + m * axis_x[i]
        ss_t += (axis_y[i] - mean_y) ** 2
        ss_t += (axis_y[i] - y_pred) ** 2

        r2 = 1 - (ss_r/ss_t)

    print('Goodness of fit using r2 method :', r2)


def main():
    print('Machine Learning / Superwised / Regression / Linear')
    HeadBrainPredictor()


if __name__ == '__main__':
    main()
