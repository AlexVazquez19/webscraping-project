# Web Scraping Project
My goal with this project was to learn how to scrape important information from different types of websites using Python, be it static HTML websites or dynamically changing pages. I was inspired to do this project because of my experience working at OmniSync where I had my first introduction to web scraping. My task was to scrape information from startup directories, academic profiles, and professor lists that we could use for client prospecting. The data I scraped ended up getting us new clients and helped the software team developing a new machine learning software tool. I really enjoyed the process of identifying useful data, extracting it, and seeing it ultimately be used by others in the company, and this project is a way for me to further pursue my interest in web scraping.

The primary libraries I use in this project are Selenium (specifically the WebDriver for Chrome), Beautiful Soup, and Requests. Below are descriptions of the websites I have scraped.

Y Combinator Startup Directory
---
From the [Y Combinator Startup Directory](https://www.ycombinator.com/companies/) I scraped the following data:
* company names
* one-line descriptions
* website link
* year founded
* location
* team size
* social links (linkedIn, Facebook, Twitter, Crunchbase)

Here is a [google spreadsheet](https://docs.google.com/spreadsheets/d/1GrnNFGHbi1ES1nWV4iymrPi_e9SBBKpDEyCVYnWkHx8/edit#gid=1678900764) with the data.

While the main directory page isn't super complex, I added an additional layer of complexity by retrieving the links for each company's page and then requesting the HTML of each page to get additional data, such as the description and year founded which are not displayed on the main directory page.

Yahoo Finance
---
I started by scraping the following data from the [Yahoo Finance Most Active stocks](https://finance.yahoo.com/most-active?count=25&offset=0) page: 
* Ticker
* Company name
* Price (Intraday)
* Change
* % Change
* Volume
* Avg Vol (3 month)
* Market Cap
* PE Ratio

Here is a [google spreadsheet](https://docs.google.com/spreadsheets/d/1xhbVqrE6CJ0y6WOII7bIvMCUlTBw0pJsvnG-wMP233Y/edit?usp=sharing) with the data from 3/27.

You might be wondering why I scraped this data using Python rather than just using the Yahoo Finance API, and it's true that the API is probably a more reliable way to retrieve the data, but I chose to scrape this page to learn how to get data that changes throughout the day and is displayed through a more complex front end. 
