from sklearn import tree

Rough = 1
Smooth = 0

Tennis = 1
Cricket = 2

BallsFeatures = [
    [35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]
]

Lables = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

classified = tree.DecisionTreeClassifier()

classified = classified.fit(BallsFeatures, Lables)

predicted = classified.predict([[44,1]])

if predicted[0] == 1:
    print('Tennis')
    print(predicted)
else:
    print('Cricket')
    print(predicted)

predicted = classified.predict([[95,0]])

if predicted[0] == 1:
    print('Tennis')
    print(predicted)
else:
    print('Cricket')
    print(predicted)