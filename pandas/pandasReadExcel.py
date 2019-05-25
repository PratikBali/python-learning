import pandas as pd

file = 'First_Excel_File_From_Python_Pandas.xlsx'
data = pd.read_excel(file, sort=False)
print(data.head())

data_sheet1 = pd.read_excel(file, sheet_name=0, index_col=0)
print(data_sheet1.head())

xlsx = pd.ExcelFile(file)
data_sheets = []

for sheet in xlsx.sheet_names:
    print(sheet)
    data_sheets.append(xlsx.parse(sheet))

data = pd.concat(data_sheets)

print(data)