import random
import os
from tabulate import tabulate
import gspread
from oauth2client.service_account import  ServiceAccountCredentials

os.chdir(os.getcwd() + "/Python/2022.11.22-google-sheet-api")

# scopes = [
#     'https://www.googleapis.com/auth/spreadsheets',
#     'https://www.googleapis.com/auth/drive',
# ]

creds = ServiceAccountCredentials.from_json_keyfile_name('./secret-key.json')
file = gspread.authorize(creds)

try:
	workspace 	= file.open("backup")
except:
    print("Something went wrong :c")
    input("Press somthing to continue...")
    quit()

sheet_file 	= workspace.sheet1
sheet_name_values	= sheet_file.range('B2:B20')
sheet_sname_values	= sheet_file.range('c2:c20')

group_a_ceils = sheet_file.range('G2:G12')
group_b_ceils = sheet_file.range('H2:H12')

name_list 	= []
group_table = [["Group A", "Group B"]]

for i in range(len(sheet_name_values)):
    name_list.append(
			#* create `Name Surename` list item
            f"{sheet_name_values[i].value} {sheet_sname_values[i].value}" 
            )

if len(name_list) % 2 == 1:
    name_list.append("Alper Tavukçu")


while len(name_list) > 0:
    index1  = int(random.random() * len(name_list))
    elem1   = name_list[index1]
    del name_list[index1]

    index2  = int(random.random() * len(name_list))
    elem2   = name_list[index2]
    del name_list[index2]

    group_table.append([elem1, elem2])

print(tabulate(group_table, headers="firstrow", tablefmt="fancy_grid"))



for i in range(len(group_table)):
    group_a_ceils[i].value = group_table[i][0]
    group_b_ceils[i].value = group_table[i][1]

# print(group_a_ceils)
# print(group_b_ceils)
sheet_file.update_cells(group_a_ceils)
sheet_file.update_cells(group_b_ceils)
