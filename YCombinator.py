import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/alejandrovazquez/Desktop/Misc./chromedriver_mac64/chromedriver")
URL = "https://www.ycombinator.com/companies/"
driver.get(URL)
time.sleep(4)

# Infinite scroller
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(.5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Get raw html of website
page_src = driver.page_source
soup = BeautifulSoup(page_src,'html.parser')
driver.quit()
company_card_container = soup.find('div',class_='q1vdpoLtJkwUT8jN22K2 dsStC1AzZueqISZqfHLZ')
company_cards = company_card_container.find_all('a',class_='WxyYeI15LZ5U_DOM0z8F no-hovercard')

# Iterate through the company cards to get the names, one-line descriptions, and URLs

company_names,one_line_descriptions,company_urls = [],[],[]

for card in company_cards:

    # Company name
    company_name = card.find('span',class_='CBY8yVfV0he1Zbv9Zwjx')
    if company_name != None:
        company_names.append(company_name.text.strip())
    else:
        company_names.append(None)

    # One-line description
    one_line = card.find('span',class_='OCTUb4j7DGmBqnUsAzVD')
    if one_line != None:
        one_line_descriptions.append(one_line.text.strip())
    else:
        one_line_descriptions.append(None)

    # Compant URL
    url = card['href']
    if url != None:
        company_urls.append('https://www.ycombinator.com' + url)
    else:
        company_urls.append(None)









'''
#Creates a CSV
dictionary = {"Company Name":company_names_notags,"One-liner":company_descriptions_notags,"Abstract":company_abstracts,"Email":company_emails}

dataframe = pd.DataFrame(dictionary)

dataframe.to_csv('webscraperv3.csv')
'''