from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import os
import numpy as np
import regex as re

# https://www.youtube.com/watch?v=IU0QtIAwkxw
# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# driver = webdriver.Chrome()
# url = 'https://www.kayak.com/flights/EWR-DEN/2024-01-26/2024-01-29?sort=bestflight_a'

url = 'https://login.yahoo.com/account/create'
browser.get(url)

# flight_rows=driver.find_element("xpath", '//div[@class="inner-grid keel-grid"]')
# print(flight_rows)

# https://stackoverflow.com/questions/72754651/attributeerror-webdriver-object-has-no-attribute-find-element-by-xpath

# https://www.browserstack.com/guide/find-element-by-xpath-in-selenium
# https://stackoverflow.com/questions/51865300/python-selenium-keep-browser-open
browser.find_element("xpath", "//input[@id='usernamereg-firstName']").send_keys("Javed")
browser.find_element("xpath", "//input[@id='usernamereg-lastName']").send_keys("Siddique")
browser.find_element("xpath", "//input[@id='usernamereg-birthYear']").send_keys("1976")
browser.find_element("xpath", "//input[@id='usernamereg-password']").send_keys("S123456!")
# browser.find_element("xpath", "//input[@id='usernamereg-userID']").send_keys("ebtrader")

# driver.findElement(By.xpath("//input[@id='usernamereg-lastName']")).sendKeys("Your-Last_name"); //xpath for last name box
# driver.findElement(By.xpath("//input[@id='usernamereg-yid']")).sendKeys("email@yahoo.com"); //xpath for email box
# driver.findElement(By.xpath("//input[@id='usernamereg-phone']")).sendKeys("123456789"); //xpath for phone number box
# driver.findElement(By.xpath("//select[@id='usernamereg-month']")).click(); //xpath for usermonth box
# driver.findElement(By.xpath("//input[@id='usernamereg-day']")).sendKeys("01"); //xpath for userday box
# driver.findElement(By.xpath("//input[@id='usernamereg-year']")).sendKeys("1999");// xpath for user year
# print(element)
