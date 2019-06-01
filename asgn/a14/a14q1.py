import pandas as pd
import csv
from sklearn import tree
from sklearn import preprocessing

overcast = 0
rainy  = 1
sunny = 2

cool = 0
hot = 1
mild = 2

no = 0
yes = 1

def myPredict(weather,temparature,play):
    # print(weather, '\n', temparature, '\n', play)
    features = list(zip(weather,temparature))                       #best
    # print(features)

    classified = tree.DecisionTreeClassifier()

    classified = classified.fit(features, play)
    predicted = classified.predict([[0,0]])

    print(predicted)
    if predicted == 1:
        print('Play')
    else:
        print('Not Play')

def main():
    weather = []
    temparature = []
    play = []
    with open('PlayPredictor.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        line_count = 0

        for row in csv_reader:
            print(row)
            if line_count == 0:
                line_count += 1

            else:
                weather.append(row[1])
                temparature.append(row[2])
                play.append(row[3])

                line_count += 1
        print(f'Processed {line_count} lines.')

    encoder = preprocessing.LabelEncoder()                          #best
    weather_encoded = encoder.fit_transform(weather)
    temparature_encoded = encoder.fit_transform(temparature)
    play_encoded = encoder.fit_transform(play)

    myPredict(weather_encoded,temparature_encoded,play_encoded)

if __name__ == "__main__":
    main()