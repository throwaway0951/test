
#This will not run on online IDE
#@CrustyPotato
import requests
from bs4 import BeautifulSoup as bs
import os,sys
import time
from fake_useragent import UserAgent
import random

class co:
    r='\033[31m' #red
    g='\033[32m' #green
    o='\033[33m' #orange
    bl='\033[34m' #blue
    p='\033[35m' #purple
    c='\033[36m' #cyan
    y='\033[93m' #yellow
    pi='\033[95m' #pink
    e= '\033[0m' #END
    b= '\033[1m' #BOLD
    u= '\033[4m' #underline

ua=UserAgent()
hdr = {'User-Agent': ua.random,
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}

class testo():
    def __init__(self):
        print (co.g + co.b + "----->         Made by @CrustyPotato      <-----")
        time.sleep(1)
        print (co.g + "----->             Version: 1.0           <-----")
        time.sleep(2)
        print (co.g + "----->     #1 tool for Background Search  <-----"+co.e)
        time.sleep(2)

def clear_text(text):
    if "\n" in text:
        text = text.replace("\n", '')
    if "\xa0" in text:
        text = text.replace("\xa0", "")
        return text
    Print(co.g+"Press"+co.e, co.r+ 'B'+co.e, co.g+'for beenverified ---WORKING---'+co.e)
    PRESS(co.g+"Press"+co.e, co.r+ 'T'+co.e, co.g+'for truthfinder ---NOT WORKING---'+co.e)
    PRESS(co.g+"Press"+co.e, co.r+ 'W'+co.e, co.g+'for whitepages ---NOT WORKING---'+co.e)
    print(co.r + co.b +'BE SURE TO USE HYPHEN(-) WHEN ENETERING NAME')
    msgstr1 = f'BE SURE TO TYPE SLASH(/) AFTER EVERY INPUT' +co.e
    #time.sleep(3)
    print (msgstr1)
    print("AFTER ENTERING INPUT IF IT SHOWS BLANK OR NONE THEN USER NOT FOUND")
    name = input("Enter the first & last name | example: james-charles/: ")
    state= input("Enter State | example: ca,pa,tx/: ")
    city = input("Enter City | example: los-angeles/: ")
    URL = 'https://www.beenverified.com/people/' +name +state +city
    r = requests.get(URL, headers=hdr)
    soup = bs(r.content, features="html.parser")
    body = soup.body
    div = body.find_all('div', {'class':'search-result card'})
    for div_ in div:
        print(co.y + "=-----------------------------------------------------------------="+ co.e)
        time.sleep(random.randint(1,3))
        name_content = div_.find('div', {'class': 'search-result__title'}).text
        print (co.bl + co.b+name_content+ co.e)
        age_content = div_.find('div', {'class': 'search-result__age age'}).text
        #print (age_content)
        name_content = name_content.split('|')
        name = clear_text(name_content[0])
        city = clear_text(name_content[1])
        print (co.pi+city+co.e)
        age = age_content.split(":")[1].strip()
        print (age)
        dl = div_.find('dl', {'class': 'search-result__list'})
        print (co.y + co.b +dl.text+co.e)
        dd = dl.span.find_all("dd")

obj=testo()
