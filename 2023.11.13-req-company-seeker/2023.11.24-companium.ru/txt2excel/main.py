import time
import re
import xlsxwriter as xl

index = 1
file_path = "./src/data464600.txt"
dist_file_name = f'./dist/excel_companium-Time:{time.time()}.xlsx'

excel = xl.Workbook(dist_file_name)
spreadsheet = excel.add_worksheet()

spreadsheet.write(f'A{index}', 'Index')
spreadsheet.write(f'B{index}', 'Name')
spreadsheet.write(f'C{index}', 'Phone')
spreadsheet.write(f'D{index}', 'Email')
spreadsheet.write(f'E{index}', 'Website')
spreadsheet.write(f'F{index}', 'Socials')
spreadsheet.write(f'G{index}', 'Data URL')

index += 1

      # file.write(f'   Index: {index}\n')
      # file.write(f'    Name: {str(data[0])}\n')
      # file.write(f'   Phone: {str(data[1])}\n')
      # file.write(f'   Email: {str(data[2])}\n')
      # file.write(f' Website: {str(data[3])}\n')
      # file.write(f' Socials: {str(data[4])}\n')
      # file.write(f'Data URL: {str(data[5])}\n\n\n')


with open(file_path, "r") as file:
  for line in file.readlines():
    if line == '\n':
      continue
    
    if 'Index' in line:
      index += 1
      spreadsheet.write(f'A{index}', line[10:-1].strip())
    elif 'Name' in line:
      spreadsheet.write(f'B{index}', line[10:-1].strip())  
    elif 'Phone' in line:
      spreadsheet.write(f'C{index}', line[10:-1].strip())
    elif 'Email' in line:
      spreadsheet.write(f'D{index}', line[10:-1].strip())
    elif 'Website' in line:
      spreadsheet.write(f'E{index}', line[10:-1].strip())
    elif 'Socials' in line:
      spreadsheet.write(f'F{index}', line[10:-1].strip())
    elif 'Data URL' in line:
      spreadsheet.write(f'G{index}', line[10:-1].strip())


excel.close()