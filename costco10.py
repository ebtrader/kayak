from selenium import webdriver
import time
import pandas as pd

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)

# https://www.costco.com/laptops.html?graphic-card=nvidia-geforce-rtx-3050+nvidia-geforce-rtx-3050ti+nvidia-geforce-rtx-3070ti+nvidia-geforce-rtx-4050+nvidia-geforce-rtx-4060+nvidia-geforce-rtx-4070+nvidia-geforce-rtx-4080&memory-(ram)=32-gb+64-gb&deliveryFacetFlag=false&refine=%7C%7CMemory__RAM__attr-32%2BGB%7C%7CMemory__RAM__attr-64%2BGB%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B3050%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B3050Ti%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B3070Ti%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4050%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4060%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4070||Graphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4080

url_path = 'https://www.costco.com/laptops.html?graphic-card=nvidia-geforce-rtx-3050+nvidia-geforce-rtx-3050ti+' \
           'nvidia-geforce-rtx-3070ti+nvidia-geforce-rtx-4050+nvidia-geforce-rtx-4060+nvidia-geforce-rtx-4070+' \
           'nvidia-geforce-rtx-4080&memory-(ram)=32-gb+64-gb&deliveryFacetFlag=false&refine=%7C%7CMemory__' \
           'RAM__attr-32%2BGB%7C%7CMemory__RAM__attr-64%2BGB%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B3050%7C%7CGraphic_Card_' \
           'attr-NVIDIA%2BGeForce%2BRTX%2B3050Ti%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B3070Ti%7C%7CGraphic_Card_' \
           'attr-NVIDIA%2BGeForce%2BRTX%2B4050%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4060%7C%7CGraphic_Card_' \
           'attr-NVIDIA%2BGeForce%2BRTX%2B4070||Graphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4080'
# Target URL
driver.get(url_path)

# To load entire webpage
time.sleep(20)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

text_file = driver.find_element("xpath", "/html/body").text


file = open('costco.txt', 'w', encoding='utf-8')

file.write(text_file)

file.close()

# Printing the whole body text
print(text_file)

# Closing the driver
driver.close()

