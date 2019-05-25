import pandas as pd
import numpy as np

s = pd.Series()
print('1', s)

data = np.array(['a','b','c','d'])
s = pd.Series(data)
print('2', s[0])

data = np.array(['a','b','c','d'])
s = pd.Series(data, index=[100,101,102,103])
print('3', s[101])

data = {'a':0.1,'b':0.2,'c':1.1,'d':2.1}
s = pd.Series(data)
print('4\n',s)