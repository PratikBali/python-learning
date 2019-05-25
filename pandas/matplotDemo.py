import pandas as pd
import matplotlib.pyplot as plot

file = 'First_Excel_File_From_Python_Pandas.xlsx'
data = pd.read_excel(file)

print('All Data')
print(data)

print('first 5 rows')
print(data.head())

print('last 5 rows')
print(data.tail())

print(data.shape)

sorted_data = data.sort_values(['Name'],ascending=False)
print('Sorted data')
print(sorted_data)

data['Fees'].plot(kind='hist')
plot.show()

data['Fees'].plot(kind='barh')
plot.show()
