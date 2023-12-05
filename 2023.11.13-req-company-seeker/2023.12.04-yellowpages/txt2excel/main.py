import time
import re
import xlsxwriter as xl

index = 1
file_path = "./src/info.md"
dist_file_name = f'./dist/yellowpages-Time:{time.time()}.xlsx'

excel = xl.Workbook(dist_file_name)
spreadsheet = excel.add_worksheet()

spreadsheet.write(f'A{index}', 'Index')
spreadsheet.write(f'B{index}', 'Name')
spreadsheet.write(f'C{index}', 'Whatsapp')
spreadsheet.write(f'D{index}', 'Website')
spreadsheet.write(f'E{index}', 'Phones')
spreadsheet.write(f'F{index}', 'Link')

#   Name: Abou Malak For Marble
# Whatsapp: 
#  Website: 
#   Phones: 0128-5735-564 0128-4932-114 
#     Link: https://yellowpages.c
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

    if 'Name' in line:
      spreadsheet.write(f'B{index}', line[10:-1].strip())  
    elif 'Whatsapp' in line:
      spreadsheet.write(f'C{index}', line[10:-1].strip())
    elif 'Website' in line:
      spreadsheet.write(f'D{index}', line[10:-1].strip())
    elif 'Phones' in line:
      spreadsheet.write(f'E{index}', line[10:-1].strip())
    elif 'Link' in line:
      spreadsheet.write(f'F{index}', line[10:-1].strip())
    else:
      spreadsheet.write(f'A{index}', index)
      index += 1


excel.close()