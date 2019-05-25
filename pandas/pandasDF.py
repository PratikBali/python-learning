import pandas as pd

print ('Demo of Series :- \n')
s = pd.Series([1,2,3])
print(s)

print ('Demo of Series with index:- \n')
s = { 'one': pd.Series([1,2,3], index=['a','b','c']),
'two': pd.Series(['x','y','z'], index=[1,2,3]), }
print(s)

print ('Demo of Empty data frame :- \n')
df = pd.DataFrame()
print(df)

print ('Demo of data frame with list:- \n')
data = [0,1,2,3,4,5]   # column without name
df = pd.DataFrame(data)
print(df)

data = {'Numbers':[0,1,2,3,4,5]}   # column with name Numbers
df = pd.DataFrame(data)
print(df)

data = {'Numbers':[0,1,2,3],'Letters':['a','b','c','d']}   # 2 columns with names
df = pd.DataFrame(data)
print(df)

data = [
    {'Name': 'PPA', 'Duration': 6, 'Fees': 6500},
    {'Name': 'LB', 'Duration': 3, 'Fees': 5000},
    {'Name': 'IPD', 'Duration': 2, 'Fees': 4000},
    {'Name': 'MOS', 'Duration': 4, 'Fees': 6000},
    {'Name': 'UNIX', 'Duration': 4, 'Fees': 'free for mos'},
    {'Name': 'ANGULAR', 'Duration': 3, 'Fees': 2500},
    {'Name': 'PYTHON', 'Duration': 3, 'Fees': 5000},]  # 3 columns with names and values
df = pd.DataFrame(data)
print(df)

print('Combination of series and data frames:')

series = { 'one': pd.Series([1,2,3], index=['a','b','c']),
'two': pd.Series(['x','y','z'], index=[1,2,3]), }
df = pd.DataFrame(series)
print(df)
print(df['one'])
print(df['two'])


