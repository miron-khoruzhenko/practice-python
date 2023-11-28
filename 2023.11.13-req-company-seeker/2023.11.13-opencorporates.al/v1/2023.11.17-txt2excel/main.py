import time
import re
import xlsxwriter as xl

index = 1
file_path = "./src/companyinvester.txt"
dist_file_name = f'excel_opencorporate-Time:{time.time()}.xlsx'

excel = xl.Workbook(dist_file_name)
spreadsheet = excel.add_worksheet()

spreadsheet.write(f'A{index}', 'Index')
spreadsheet.write(f'B{index}', 'Name')
spreadsheet.write(f'C{index}', 'Website')
spreadsheet.write(f'D{index}', 'Email')
spreadsheet.write(f'E{index}', 'Phone')
spreadsheet.write(f'F{index}', 'ID')

index += 1

def find_pattern(data_string):
  index_pattern = r'^(\d+)'
  company_name_pattern = r'\d+\s(.*?)(?:\s+http|www|\s+\S+@\S+|None)'
  
  website_pattern = r'(http|www)\S+'
  email_pattern = r'(\S+@\S+)'
  phone_pattern = r'(\S+@\S+|None|\s\s|tel:)\s+(.*?)\s+id:'
  company_id_pattern = r'id:\s+(\S+)'

  # Applying each regex to the data string
  index_match = re.search(index_pattern, data_string)
  company_name_match = re.search(company_name_pattern, data_string)
  email_match = re.finditer(email_pattern, data_string)
  website_match = re.finditer(website_pattern, data_string)
  phone_match = re.search(phone_pattern, data_string)
  company_id_match = re.search(company_id_pattern, data_string)

  website_array = [match.group() for match in website_match]
  email_array = [match.group() for match in email_match]
  # print(email_array)

  extracted_data_separate = {
      "index": index_match.group(1) if index_match else None,
      "company_name": company_name_match.group(1).strip() if company_name_match else None,
      # "website": website_match.group(0) if website_match else None,
      "website": ' '.join(website_array) if len(website_array) > 0 else None,
      # "email": email_match.group(1) if email_match else None,
      "email": ' '.join(email_array) if len(email_array) > 0 else None,
      # "email": email_match.group(1) if email_match else None,
      "phone": phone_match.group(2) if phone_match else None,
      # "phone2": phone2_match.group(0) if phone2_match else None,
      "company_id": company_id_match.group(1) if company_id_match else None
  }

  return extracted_data_separate


with open(file_path, "r") as file:
  for line in file.readlines():
    if line == '\n':
      continue

    try:
      data = find_pattern(line)
    except Exception as e:
      print(str(e) + '\n')
    spreadsheet.write(f'A{index}', data['index'])
    spreadsheet.write(f'B{index}', data['company_name'])  
    spreadsheet.write(f'C{index}', data['website'])
    spreadsheet.write(f'D{index}', data['email'])
    spreadsheet.write(f'E{index}', data['phone'])
    spreadsheet.write(f'F{index}', data['company_id'])

    index += 1
    # if index == 10:
    #   break

excel.close()