import time
import re
import xlsxwriter as xl

index = 1
source_file_path = "../dist/joined/link1.txt"
dist_file_name = f'./distExcel/excel_opencorporates-Time:{time.time()}.xlsx'

excel = xl.Workbook(dist_file_name)
spreadsheet = excel.add_worksheet()

spreadsheet.write(f'A{index}', 'Index')
spreadsheet.write(f'B{index}', 'Name')
spreadsheet.write(f'C{index}', 'Website')
spreadsheet.write(f'D{index}', 'Email')
spreadsheet.write(f'E{index}', 'Phone')
spreadsheet.write(f'F{index}', 'Data URL')

index += 1



with open(source_file_path, "r") as file:
  for line in file.readlines():
    if line == '\n':
      continue
    
    if 'Index' in line:
      index += 1
      spreadsheet.write(f'A{index}', line[7:-1].strip())
    elif 'Name' in line:
      spreadsheet.write(f'B{index}', line[7:-1].strip())  
    elif 'URL' in line:
      spreadsheet.write(f'C{index}', line[7:-1].strip())
    elif 'Email' in line:
      if 'None' in line:
        continue

      spreadsheet.write(f'D{index}', line[7:-1].strip())
    elif 'Phone' in line:
      spreadsheet.write(f'E{index}', line[7:-1].strip())
    elif 'ID' in line:
      spreadsheet.write(f'F{index}', 'https://www.opencorporates.al/sq/nipt/' + line[7:-1].strip())


excel.close()