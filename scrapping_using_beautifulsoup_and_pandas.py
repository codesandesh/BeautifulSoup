import requests
from bs4 import BeautifulSoup
import re 
import pandas  as pd 
url='https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
response=requests.get(url)
if response.status_code>=200 and response.status_code<300:
    soup=BeautifulSoup(response.text,'lxml')
    all_product=[]
    all_p_tags=soup.find_all('a', class_='title')
    for i in all_p_tags:
        all_product.append(i.text)
    # for j in all_product:
    
    #     print(j)
    # print(len(all_product))
    all_price=[]
    all_price_value=soup.find_all('h4',class_="price float-end card-title pull-right")
    for  j in all_price_value:
        all_price.append(j.text)

    data={'name_of_the_product':all_product,'price_of_the_product':all_price}
    df=pd.DataFrame(data)
    
else:
    print(' we do not  have  authority to  scrab  web  site !!!! sorry  for inconvinence')
print(df)

df.to_excel('laptop_data.xlsx',index=True) 