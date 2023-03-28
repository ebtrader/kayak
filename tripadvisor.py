from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
# options.add_argument('--headless')
options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver = webdriver.Chrome(options=options)
import time

driver.get("https://www.tripadvisor.com/Airline_Review-d8729157-Reviews-Spirit-Airlines#REVIEWS")
# more_buttons = driver.find_elements("name", "moreLink")
# for x in range(len(more_buttons)):
#     if more_buttons[x].is_displayed():
#         driver.execute_script("arguments[0].click();", more_buttons[x])
#         time.sleep(1)
page_source = driver.page_source
# print(driver.page_source)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page_source, 'lxml')
# print(soup.prettify())

reviews = []
# reviews_selector = soup.find_all('div', class_='reviewSelector')
reviews_selector = soup.find_all('div', class_='aBbCw b S4 H4')
print(reviews_selector)
# for review_selector in reviews_selector:
#     review_div = review_selector.find('div', class_='dyn_full_review')
#     print(review_div)

#     if review_div is None:
#         review_div = review_selector.find('div', class_='basic_review')
#     review = review_div.find('div', class_='entry').find('p').get_text()
#     review = review.strip()
#     reviews.append(review)

# print(reviews)
