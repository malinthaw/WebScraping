from bs4 import BeautifulSoup
import requests
import time

def find_altos():
    htlm_text = requests.get('https://ikman.lk/en/ads/sri-lanka/cars?sort=relevance&buy_now=0&urgent=0&query=alto').text
    soup = BeautifulSoup(htlm_text,'lxml')
    vehicles = soup.find_all('li', class_= 'normal--2QYVk gtm-normal-ad')
    for vehicle in vehicles:
        vehicle_price = vehicle.find('div', class_='price--3SnqI color--t0tGX').text.replace(' ','')
        # vehicle_type = vehicle.find('h2', class_='heading--2eONR heading-2--1OnX8 title--3yncE block--3v-Ow').text
        vehicle_odo = vehicle.find('div').text
        # print(f"Vehicle_type: {vehicle_type.strip()}")
        print(f"Vehicle_Price: {vehicle_price.strip()}")
        print(f"vehicle_Details: {vehicle_odo.strip()}")



if __name__ == '__main__':
    while True:
        find_altos()
        time_wait = 10
        print(f"Waiting {time_wait} minitues...")
        time.sleep(time_wait * 60)


