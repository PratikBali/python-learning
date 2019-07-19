import numpy as np
import pandas as pd
import matplotlib.pyplot as plot


def MyPredictor():

    # Load Data
    axis_x = [1, 2, 3, 4, 5]
    axis_y = [3, 4, 2, 4, 5]

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

    # Display plotting of above points
    x = np.linspace(1, 6, n)

    y = m * x + c

    plot.plot(x, y, color='#58b970', label='Regression line')
    plot.scatter(axis_x, axis_y, color='#ef5423', label='Scatter plot')

    plot.xlabel('X - Independant variable')
    plot.ylabel('Y - Dependant variable')

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
    MyPredictor()


if __name__ == '__main__':
    main()
