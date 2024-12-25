import requests
from bs4 import BeautifulSoup
url='https://webscraper.io/test-sites/e-commerce/allinone'
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')
all_content=soup.find_all('a')
# print(all_content)
all_specific_div=soup.div.p.string
print(all_specific_div)
