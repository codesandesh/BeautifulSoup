import pandas as pd
from bs4 import  BeautifulSoup
import re 
import requests

url='https://webscraper.io/test-sites/e-commerce/allinone'
response=requests.get(url)
if response.status_code>=200 and  response.status_code<300:
    soup=BeautifulSoup(response.text,'lxml')
    all_nav_item=soup.find('ul',class_='nav flex-column',id='side-menu')
    
else:
    print('we are not  able  to scrap the  web  page  that  you had  given !!!! sorry  for  inconvinience ')

# print(all_nav_item)
for i in all_nav_item:
    print(i.text)

    

