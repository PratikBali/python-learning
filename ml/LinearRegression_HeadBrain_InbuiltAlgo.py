import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

border = '* ' * 50


def HeadBrainPredictor():
    # Load data
    data = pd.read_csv('../datasets/DatasetHeadBrain.csv')

    # Size
    print(border)
    print('Size of data set head brain', data.shape)

    # Prepare data
    axis_x = data['Head Size(cm^3)'].values
    axis_y = data['Brain Weight(grams)'].values

    axis_x = axis_x.reshape((-1, 1))

    n = len(axis_x)

    reg = LinearRegression()

    reg.fit(axis_x, axis_y)

    predicted = reg.predict(axis_x)

    r2 = reg.score(axis_x, axis_y)

    # Goodness of fit
    print(f'Goodness of fit {r2}')


def main():
    print(border)
    print('Macine Learning / Superwised / Regression / Linear')
    HeadBrainPredictor()


if __name__ == "__main__":
    main()
