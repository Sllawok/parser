"""Пример работы с beautifulsoup"""
# 1. регулярные выражения
# 2. сторонние библиотеки beautifulsoup, lxml
# 3. scrapy
import requests
from bs4 import BeautifulSoup

url = 'https://auto.drom.ru/region38/toyota/'

response = requests.get(url)

# Создаем суп для разбора html
soup = BeautifulSoup(response.text, 'html.parser')


site_0 = soup.find('h1', class_ = 'css-1p6sxhz e18vbajn0')
for site_1 in site_0:
    print(site_1)

name = soup.find('span',class_='css-ik080n e162wx9x0')

count = soup.find('span',class_ = 'css-9qy7tn ebqjjri5')
for ii in count:
 print()

for i in name:
 print('Кол-во: ',i,'=>',ii)

