from selenium import webdriver
from bs4 import BeautifulSoup

# https://analyticsindiamag.com/beautiful-soup-webscraping-python/

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get('https://analyticsindiamag.com/')

source_code=driver.page_source

soup = BeautifulSoup(source_code, 'lxml')
# print(soup.prettify())

article_block = soup.find_all('div', class_='post-title')
print(article_block)

for titles in article_block:
    title = titles.find('span').get_text()
    # print(title)
