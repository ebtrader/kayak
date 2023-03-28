from selenium import webdriver

# https://towardsdatascience.com/how-to-find-cheap-flights-in-80-lines-of-code-ba4f492587db

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
# options.add_argument('--headless')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

import time

driver.get("https://www.kayak.com/flights/EWR-DEN/2023-05-31?sort=bestflight_a")
time.sleep(15)
page_source = driver.page_source

from bs4 import BeautifulSoup

soup = BeautifulSoup(page_source, 'html.parser')
print(soup.prettify())

# prices = []
# price = soup.find_all('div',class_='Flights-Results-FlightPriceSection right-alignment sleek')
# print(price)

# for i in price:
#     for j in i.find_all('span', class_='price-text'):
#         prices.append(j.text)
# print(prices)
