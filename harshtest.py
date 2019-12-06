import requests
from bs4 import BeautifulSoup as bs

class co:
    r='\033[31m' #red
    g='\033[32m' #green
    o='\033[33m' #orange
    b='\033[34m' #blue
    p='\033[35m' #purple
    c='\033[36m' #cyan
    y='\033[93m' #yellow
    p='\033[95m' #pink
    e= '\033[0m' #END
    b= '\033[1m' #BOLD


def clear_text(text):
    if "\n" in text:
        text = text.replace("\n", '')
    if "\xa0" in text:
        text = text.replace("\xa0", "")
    return text

print('Be sure to use hyphen(-) enetering name')
msgstr1 = f'Be sure to type slash(/) after every input{co.e}'
print (msgstr1)
# name = input("Enter the first & last name | example: james-charles/: ")
# state = input("Enter State | example: ca,pa,tx/: ")
# city = input("Enter City | example: los-angeles/: ")
URL = 'https://www.beenverified.com/people/donald-duck'
r = requests.get(URL)
soup = bs(r.content, features="html.parser")
body = soup.body
div = body.find_all('div', {'class':'search-result card'})
for div_ in div:
    print("=-----------------------------------------------------------------=")
    name_content = div_.find('div', {'class': 'search-result__title'}).text
    age_content = div_.find('div', {'class': 'search-result__age age'}).text
    name_content = name_content.split('|')
    name = clear_text(name_content[0])
    city = clear_text(name_content[1])
    age = age_content.split(":")[1].strip()
    dl = div_.find('dl', {'class': 'search-result__list'})
    dd = dl.span.find_all("dd")
    print(dd)