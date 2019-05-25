import pandas as pd
import numpy as np

series1 = pd.Series([1,2,3], index=['a','b','c'])
series2 = pd.Series(['x','y','z'], index=[1,2,3])

df1 = { 'one': series1, 'two': series2}
df2 = { 'one': series1, 'two': series2}

data = {'item1': df1, 'item2':df2}

panel = pd.Panel(data)
# panel.to_frame()
print(panel)
