import random
import pandas as pd
import os
from tabulate import tabulate

os.chdir(os.getcwd() + "/Python/2022.12.28-twitter-api")

require_col = [i for i in range(11)]
# datasheet = pd.read_excel('backup.xlsx', usecols=require_col, skiprows=1)
datasheet = pd.read_excel('twitterDataset.xlsx', usecols=require_col)
# print(datasheet.head())

# datalist = datasheet.columns
# datalist = datasheet.columns.values
# datalist = datasheet.values
datalist = datasheet.columns

# print(datalist)
print(datalist)
# print(len(datalist))



# input('End of the program')
