import pandas as pd
import xlrd
import csv

pathToXlsx = r'C:\Users\marti\Desktop\PythonProjects\AxieInfinity\AxieDetails.xlsx'
pathToNewCsv = 'AxieDetails.csv'

def T1():
    read_file = pd.read_excel (pathToXlsx)
    read_file.to_csv (pathToNewCsv, index=None, header=True)

def T2():
    wb = xlrd.open_workbook(pathToXlsx, engine='openpyxl')
    sh = wb.sheet_by_name('Sheet3')
    your_csv_file = open(pathToNewCsv, 'w')
    wr = csv.writer(your_csv_file)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

def T3():
    data_xls = pd.read_excel(pathToXlsx, 'Sheet3', dtype=str, index_col=None)
    data_xls.to_csv(pathToNewCsv, encoding='utf-8', index=False)


T3()