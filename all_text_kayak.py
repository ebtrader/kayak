from selenium import webdriver
import time

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)

# Target URL
driver.get('https://www.kayak.com/flights/JFK-SFO/2023-05-25/2023-06-03?sort=bestflight_a')
# To load entire webpage
time.sleep(5)

# Printing the whole body text
print(driver.find_element("xpath", "/html/body").text)

# Closing the driver
driver.close()

