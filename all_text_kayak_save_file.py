from selenium import webdriver
import time

# https://www.geeksforgeeks.org/get-all-text-of-the-page-using-selenium-in-python/

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)

# Target URL
driver.get('https://www.kayak.com/flights/EWR-DEN/2023-05-25/2023-06-03?sort=bestflight_a')
# To load entire webpage
time.sleep(15)

text_file = driver.find_element("xpath", "/html/body").text

file = open('kayak.txt', 'w')

file.write(text_file)

file.close()

# Printing the whole body text
print(text_file)

# Closing the driver
driver.close()

