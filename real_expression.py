import requests
from  bs4  import BeautifulSoup
import re 

url='https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
response=requests.get(url)
if response.status_code>=200 and response.status_code<300:
  soup=BeautifulSoup(response.text,'lxml')
  finding_lenevo=soup.find_all('a',string=re.compile('Lenovo',re.IGNORECASE))
  print(finding_lenevo)
  print(len(finding_lenevo))
else:
  print('we can not  scrap  that  web page ')
