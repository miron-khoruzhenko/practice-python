from get_infos import get_infos
import time
import time
import requests
from bs4 import BeautifulSoup
import json
import xlsxwriter as xl
import time

# out_file = open("out.csv","w","utf-8")
close =0
index = 1

excel = xl.Workbook(f'orgpage{int(index / 2)}-{time.time()}.xlsx')
spreadsheet = excel.add_worksheet()

try:
    with open("./linksAllLinks.txt","r") as file:
        
        lines_list = list(file.readlines())
        lines_list = lines_list[int(len(lines_list)/2)+25000:int(len(lines_list)/2)+26000]#* BURAYI DUZELT

        for link in lines_list:
            
            link = link.strip()
            print(link)
            com = get_infos(link)

            for key in com:
                if key == 'phones':
                    
                    for phone in com[key]:
                        spreadsheet.write(f'A{index}', phone)
                        index += 1
                    continue

                spreadsheet.write(f'A{index}', com[key])

                index += 1
            index += 2

            close+=1
            print(close)

            print("Name   : ",com["name"])
            print("Phones : ",com["phones"])
            print("Site   : ",com["site"])
            print("Mail   : ",com["mail"])
            print()
            #time.sleep()
except Exception as e:
    print(e)
    excel.close()
excel.close()
