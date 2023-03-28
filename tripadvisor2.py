from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
# options.add_argument('--headless')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

url = 'https://www.tripadvisor.in/Hotels-g28932-Hawaii-Hotels.html'
driver.get(url)
page_source = driver.page_source

from bs4 import BeautifulSoup

soup = BeautifulSoup(page_source, 'lxml')
print(soup.prettify())

reviews = []
for review in soup.findAll('a',{'class':'review_count'}):
    reviews.append(review.text.strip())
# print(reviews)
