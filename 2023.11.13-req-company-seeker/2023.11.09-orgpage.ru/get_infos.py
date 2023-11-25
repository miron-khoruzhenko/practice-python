import requests
from bs4 import BeautifulSoup

#test_url = "https://www.orgpage.ru/moskva/beyosa-6113958.html"

def get_infos(url) -> dict:
    
    company = dict()

    r = requests.get(url=url)
    soup = BeautifulSoup(r.content,"html.parser")

    con = soup.find("ul",attrs={"class" : "company-information__row"})

    #Name
    name_header = soup.find("div" ,attrs={"class":"company-header__row"})
    name_div  = name_header.find("h1",attrs={"itemprop":"name"})
    span = name_div.find("span")
    if span != None : span.replace_with("")
    name = name_div.text
    company["name"] = name.strip().strip('ООО').strip('ИП').strip()
    #print(name.strip())
        
    #Phones
    try:
        ul_phones = soup.find("ul",attrs={"class" : "company-information__phone-list"})
        spans = ul_phones.find_all("span",attrs={"class":"company-information__phone"})
        phones = [phone.text.strip() for phone in spans]
        company["phones"] = (phones)
    except:
        company["phones"] = []
    #Site
    info_div = soup.find("div",attrs={"class":"company-information__site"})
    try:
        site = info_div.find("a",attrs={"class":"nofol-link"}).get("href")
        company["site"] = site
        #print(site)
    except:
        company["site"] = None

    #Mail
    try:
        mail_element = info_div.find("p",attrs={"class":"email"})
        mail = info_div.find("a",attrs={"itemprop":"email"}).text.strip()
        #print(mail)
        company["mail"] = mail
    except:
        company["mail"] = None

    return company

    


#Test
