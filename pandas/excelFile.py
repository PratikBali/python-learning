import os
import fnmatch
from sys import *
import xlsxwriter

argc = 2

def ExcelCreate(arg):
    print(arg)
    workbook = xlsxwriter.Workbook(arg)
    worksheet = workbook.add_worksheet()

    worksheet.write('A1','Name')
    worksheet.write('B1','College')
    worksheet.write('C1','Mail')
    worksheet.write('D1','Contact')

    worksheet2 = workbook.add_worksheet()

    worksheet2.write('A1','Book')
    worksheet2.write('B1','isbn')
    worksheet2.write('C1','Author')
    worksheet2.write('D1','Publisher')
    print('done')

    workbook.close()

def main():
    if len(argv) != argc:
        print('Argument length must be ', argc)
        exit()

    try:
        ExcelCreate(argv[1])
    except Exception as e:
        print('ERROR: Eception occurred : ', e)

if __name__ == '__main__':
    main()
