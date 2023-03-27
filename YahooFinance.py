import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://finance.yahoo.com/most-active"
r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')
table = soup.find('div',id='scr-res-table')
table_body = table.find('tbody')
rows = table_body.find_all('tr')

for row in rows:
    row_data = row.find_all('td')
    for i in range(len(row_data)):
        print(row_data[i]['aria-label'])
    break
