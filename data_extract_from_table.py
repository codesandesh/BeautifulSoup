import requests
from bs4 import BeautifulSoup
import re 
import pandas  as  pd 
url='https://merolagani.com/latestmarket.aspx#google_vignette'
response=requests.get(url)
if response.status_code>=200 and response.status_code<300:
    soup=BeautifulSoup(response.text,'lxml')
    table=soup.find('table',class_='table table-hover live-trading sortable')
    header=table.find('thead')
    all_header_tr=header.find('tr')
    all_header_title=all_header_tr.find_all('th')
    all_the_tr_from_body=soup.find_all('tr')



    
   
else:
    print('we are not  allowed  to scrap the  web page !!! sorry for inconvinence ')

header_list=[]
for i in all_header_title:
    header_list.append(i.text)
print(header_list)
dict={}
catch=0
for i in all_the_tr_from_body[1:]:
    dict[str(catch)]=i.text
    catch+=1

print(dict)



