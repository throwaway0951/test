
#This will not run on online IDE
import requests
from bs4 import BeautifulSoup
import os,sys
import time
import platform

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

class testo():
    def ver(self):
        print ""
        time.sleep(0.1)
        print co.b + co.g + "----->         Made by @CrustyPotato      <-----"
        time.sleep(0.1)
        print co.y + "----->             Version: 1.0           <-----"
        time.sleep(0.1)
        print co.y + "----->     #1 tool for Background Search  <-----"
        time.sleep(0.3)
    def options(self):
        #print co.b + co.o ("Enter 1 for whitepages >>UNDER DEVELOPMEMT<<")
        #print co.b + co.o ("Enter 2 for beenverified")
        main = raw_input("Enter your choice: ")
        if main == "1":
            print co.r + co.b + 'Be sure to use hyphen(-) enetering name'
            time.sleep(0.4)
            print ('Be sure to type slash(/) after every input') + co.e
            name = raw_input("Enter the first & last name | example: james-charles/: ")
            state = raw_input("Enter State | example: ca,pa,tx/: ")
            city = raw_input("Enter City | example: los-angeles/: ")
            URL = 'https://www.beenverified.com/people/'+ name + state +city
            r = requests.get(URL)
            soup = BeautifulSoup(r.content, 'html5lib')
            a= soup.find('title')
            print (a.string)
            div = soup.find('div', id='results')
            print (div.string)
        elif main == "2":
            print ("UNDER DEVELOPMEMT")
        else:
            print ("CHECK YOUR INPUT")

obj=testo()
obj.ver()
obj.options()
