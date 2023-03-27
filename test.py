import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# Get the HTML content
url = "https://finance.yahoo.com/most-active?count=25&offset=25"
driver = webdriver.Chrome(executable_path="/Users/alejandrovazquez/Desktop/Misc./chromedriver_mac64/chromedriver")
driver.get(url)
time.sleep(6)

page_src = driver.page_source
soup = BeautifulSoup(page_src,'html.parser')
driver.quit()
symbol=[]
table = soup.find('div',id='scr-res-table')
table_body = table.find('tbody')
rows = table_body.find_all('tr')

for row in rows:
    row_data = row.find_all('td')
    for i in range(len(row_data)):
        if row_data[i]['aria-label'] == 'Symbol':
            symbol.append(row_data[i].text)

print(symbol)