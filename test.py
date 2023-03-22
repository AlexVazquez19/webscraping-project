import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

page = requests.get('https://www.ycombinator.com/companies/11874')
soup = BeautifulSoup(page.content, "html.parser")
if 'Internal Server Error' in str(soup):
    print('true')
else:
    print('false')
