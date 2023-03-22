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
    time.sleep(.75)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Get raw html of website
page_src = driver.page_source
main_soup = BeautifulSoup(page_src,'html.parser')
driver.quit()
company_card_container = main_soup.find('div',class_='q1vdpoLtJkwUT8jN22K2 dsStC1AzZueqISZqfHLZ')
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

# Iterate through each company page to collect additional data

company_descriptions,company_websites,years_founded,company_sizes,company_locations = [],[],[],[],[]

loading_tracker = 0
for url in company_urls:

    # Get the pages HTML content
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    if 'Internal Server Error' in str(soup):
        company_descriptions.append(None)
        company_websites.append(None)
        years_founded.append(None)
        company_sizes.append(None)
        company_locations.append(None)
        continue

    # Company description
    description = soup.find('p',class_='whitespace-pre-line')
    if description != None:
        company_descriptions.append(description.text.strip())
    else:
        company_descriptions.append(None)

    # Company website
    website = soup.find('a',class_='mb-2 whitespace-nowrap md:mb-0')
    if website != None:
        company_websites.append(website['href'])
    else:
        company_websites.append(None)

    # Get the data from the card on the right (includes year founded, team size, location)
    right_card = soup.find('div',class_='ycdc-card space-y-1.5 sm:w-[300px]')
    card_data = right_card.find_all('div',class_='flex flex-row justify-between')
    for i in range(len(card_data)): 
        card_data[i] = card_data[i].text
    
    # Year founded
    year = card_data[0][8:]
    years_founded.append(year)

    # Team size
    team_size = card_data[1][10:]
    company_sizes.append(team_size)

    # Location
    location = card_data[2][9:]
    company_locations.append(location)

    loading_tracker+=1
    print(loading_tracker)


# Creates a DataFrame
dictionary = {"Company Name":company_names,"One-liner":one_line_descriptions,
    "Description":company_descriptions,"Website":company_websites,
    "Year Founded":years_founded,"Location":company_locations,
    "Team Size":company_sizes}

dataframe = pd.DataFrame(dictionary)

dataframe.to_csv('YCombinator.csv') # CSV File
dataframe.to_excel('YCombinator.xlsx') # Excel File