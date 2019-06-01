import pandas as pd
import csv
from sklearn import tree
from sklearn import preprocessing

weather = {}
temparature = {}
play = {}

def mypredict():

    # classified = tree.DecisionTreeClassifier()

    # classified = classified.fit(BallsFeatures, Lables)

    # predicted = classified.predict([[44,1]])

def main():
    with open('PlayPredictor.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        print('csv_reader',csv_reader)

        line_count = 0

        for row in csv_reader:
            # print('hi')
            print('row',row)
            if line_count == 0:
                # print(f'Column names are \n \t{", ".join(row)}')
                line_count += 1

            else:
                # print(f'\t {row[0]} \t {row[1]} \t\t {row[2]} \t\t {row[3]} ')
                weather = row[1]

                line_count += 1
        print(f'Processed {line_count} lines.')

        # pd_csv = pd.read_csv(csv_file)
        # print('pd_csv',pd_csv)

    print(weather)
    # encoder = preprocessing.LabelEncoder()
    # weather = encoder.fit_transform(weather)

    mypredict()

if __name__ == "__main__":
    main()
