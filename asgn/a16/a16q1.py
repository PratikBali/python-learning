import pandas as pd
from sklearn.linear_model import LinearRegression


def main():
    # Load data
    csv_file = ('Advertising.csv')
    data = pd.read_csv(csv_file)
    print(data.head())
    print('Size of data set head brain', data.shape)

    # Clean data
    data = data.drop("Unnamed: 0", axis=1)
    print(data.head())
    print('Size of data set head brain', data.shape)

    # Prepare Data
    features = data.drop("sales", axis=1)
    print(features.head())
    target = data["sales"]
    print(target.head())


if __name__ == "__main__":
    main()
