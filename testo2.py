import requests
from bs4 import BeautifulSoup

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


print 'Be sure to use hyphen(-) enetering name'
print ('Be sure to type slash(/) after every input') + co.e
name = raw_input("Enter the first & last name | example: james-charles/: ")
state = raw_input("Enter State | example: ca,pa,tx/: ")
city = raw_input("Enter City | example: los-angeles/: ")
URL = 'https://www.beenverified.com/people/'+ name + state +city
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
a= soup.find('title')
print (a.string)
div = soup.find_all('div', {'class':'search-result__title'})
print (div.string)
