from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 25)
kayak = 'https://www.kayak.com/flights/JFK-SFO/2023-05-25/2023-06-03?sort=bestflight_a'
driver.get(kayak)

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.LJTSM3-v-d")))

# wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[46]/div[3]/div/button'))).click()

xp_prices = '//a[@class="booking-link "]/span[@class="price option-text"]/span[@class="price-text"][not(contains(@id,"extra-info"))]'
prices = wait.until(EC.presence_of_all_elements_located((By.XPATH,xp_prices)))
for price in prices:
    print(price.text)