from turtle import title

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

altovehicle = []

for x in range(1,29):
    url = 'https://ikman.lk/en/ads/sri-lanka/vehicles?sort=relevance&buy_now=0&urgent=0&query=alto&page='
    r = requests.get(url+str(x))
    soup = BeautifulSoup(r.content,'html.parser')
    # print(soup.title)
    content = soup.find_all('li', class_="normal--2QYVk gtm-normal-ad")

    for vehicle in content:
        title = vehicle.find('h2').text
        price = vehicle.find('div',class_='price--3SnqI color--t0tGX').text
        Desc =  vehicle.find('div',class_="description--2-ez3").text.replace('Cars','')

        # print(title, price, Desc)

        vehicle_info = {
            'title': title,
            'price': price,
            'Desc': Desc
        }
        altovehicle.append(vehicle_info)
    print('Alto Vehicles Found :',len(altovehicle))
    time.sleep(2)

df = pd.DataFrame(altovehicle)
print(df.head())

df.to_csv('altovehicle.csv')