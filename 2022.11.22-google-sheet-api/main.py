import random
import pandas as pd
import os
from tabulate import tabulate
import gspread
from oauth2client.service_account import  ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

creds = ServiceAccountCredentials.from_json_keyfile_name('./secret-key.json')



os.chdir(os.getcwd() + "/Python/2022.11.22-google-sheet-api")
# print(os.getcwd())

require_col = [1, 2]
# datasheet = pd.read_excel('backup.xlsx', usecols=require_col, skiprows=1)
datasheet = pd.read_excel('backup.xlsx', usecols=require_col)

# datalist = datasheet.columns
# datalist = datasheet.columns.values
datalist = datasheet.values
namelist = []

for i in range(len(datalist)):
    namelist.append(" ".join(datalist[i])) 

if len(namelist) % 2 == 1:
    namelist.append(" ")

group_table = [["Group A", "Group B"]]

while len(namelist) > 0:
    index1  = int(random.random() * len(namelist))
    elem1   = namelist[index1]
    del namelist[index1]

    index2  = int(random.random() * len(namelist))
    elem2   = namelist[index2]
    del namelist[index2]

    group_table.append([elem1, elem2])

print(tabulate(group_table, headers="firstrow", tablefmt="fancy_grid"))




input()
