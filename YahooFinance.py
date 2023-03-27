#TODO address dulicate tickers in symbol list
#TODO Test for data correctness
#TODO convert dataframe to CSV

import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# Setup path for Chrome webdriver
driver = webdriver.Chrome(executable_path="/Users/alejandrovazquez/Desktop/Misc./chromedriver_mac64/chromedriver")

# Get the HTML content
url = "https://finance.yahoo.com/most-active?count=25&offset=0"
driver.get(url)
time.sleep(6)
page_src = driver.page_source
soup = BeautifulSoup(page_src,'html.parser')

# Get the number of results loaded in the table
num_results = soup.find('span',class_='Mstart(15px) Fw(500) Fz(s)')
if num_results == None:
    print("Error: could not get the number of results")
    exit()
num_results = int(num_results.text[-11:-8])

# Get the url for each page of the table
urls = []
for i in range(25, num_results, 25):
    urls.append('https://finance.yahoo.com/most-active?count=25&offset=' + str(i))

# Lists to store the stock data
symbol,name,price_intraday,change,percent_change,volume,avg_vol_3m,market_cap,\
    pe_ratio = [],[],[],[],[],[],[],[],[]

# Function that gets the data from a given row
def get_row_data(row_data):
    for i in range(len(row_data)):
        if row_data[i]['aria-label'] == 'Symbol':
            symbol.append(row_data[i].text)
        if row_data[i]['aria-label'] == 'Name':
            name.append(row_data[i].text)
        if row_data[i]['aria-label'] == 'Price (Intraday)':
            price_intraday.append(row_data[i].text)
        if row_data[i]['aria-label'] == 'Change':
            change.append(row_data[i].text)
        if row_data[i]['aria-label'] == '% Change':
            percent_change.append(row_data[i].text)
        if row_data[i]['aria-label'] == 'Volume':
            volume.append(row_data[i].text)
        if row_data[i]['aria-label'] == 'Avg Vol (3 month)':
            avg_vol_3m.append(row_data[i].text)
        if row_data[i]['aria-label'] == 'Market Cap':
            market_cap.append(row_data[i].text)
        if row_data[i]['aria-label'] == 'PE Ratio (TTM)':
            pe_ratio.append(row_data[i].text)
            
# Get the table content from the first page
table = soup.find('div',id='scr-res-table')
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    row_data = row.find_all('td')
    get_row_data(row_data)

# Get the tables from the additional pages (if any)
for url in urls:
    driver.get(url)
    time.sleep(6) # allow time for website to fully load
    page_src = driver.page_source
    soup = BeautifulSoup(page_src,'html.parser')
    table = soup.find('div',id='scr-res-table')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        row_data = row.find_all('td')
        get_row_data(row_data) 
driver.quit()

# Create a DataFrame
dict = {"Symbol":symbol, "Name":name, "Price (Intraday)":price_intraday, 
    "Change":change, "% Change":percent_change, "Volume":volume, 
    "Avg Vol (3 Month)":avg_vol_3m, "Market Cap":market_cap, 
    "PE Ratio (TTM)":pe_ratio}

dataframe = pd.DataFrame(dict)
print(dataframe)