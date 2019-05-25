import pandas as pd

data = [
    {'Name': 'PPA', 'Duration': 6, 'Fees': 6500},
    {'Name': 'LB', 'Duration': 3, 'Fees': 5000},
    {'Name': 'IPD', 'Duration': 2, 'Fees': 4000},
    {'Name': 'MOS', 'Duration': 4, 'Fees': 6000},
    {'Name': 'UNIX', 'Duration': 4, 'Fees': 3000},
    {'Name': 'ANGULAR', 'Duration': 3, 'Fees': 2500},
    {'Name': 'PYTHON', 'Duration': 3, 'Fees': 5000}]  # 3 columns with names and values
df = pd.DataFrame(data)
print(df)

writer = pd.ExcelWriter('First_Excel_File_From_Python_Pandas.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1')

writer.save()
