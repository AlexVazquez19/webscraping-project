import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/alejandrovazquez/Desktop/Misc./chromedriver_mac64/chromedriver")
URL = "https://www.ycombinator.com/companies/"
driver.get(URL)
time.sleep(4)

# Get raw html of website
page_src = driver.page_source
soup = BeautifulSoup(page_src,'html.parser')
driver.quit()
test = soup.find('div',class_='testing')

print(test)

testing = []
testing.append(None)
testing.append('hello')
testing.append(None)
print(testing)
