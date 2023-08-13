from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

url_path = 'https://www.costco.com/laptops.html?graphic-card=nvidia-geforce-rtx-3050+nvidia-geforce-rtx-3050ti+' \
           'nvidia-geforce-rtx-3070ti+nvidia-geforce-rtx-4050+nvidia-geforce-rtx-4060+nvidia-geforce-rtx-4070+' \
           'nvidia-geforce-rtx-4080&memory-(ram)=32-gb+64-gb&deliveryFacetFlag=false&refine=%7C%7CMemory__' \
           'RAM__attr-32%2BGB%7C%7CMemory__RAM__attr-64%2BGB%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B3050%7C%7CGraphic_Card_' \
           'attr-NVIDIA%2BGeForce%2BRTX%2B3050Ti%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B3070Ti%7C%7CGraphic_Card_' \
           'attr-NVIDIA%2BGeForce%2BRTX%2B4050%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4060%7C%7CGraphic_Card_' \
           'attr-NVIDIA%2BGeForce%2BRTX%2B4070||Graphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4080'   # Update this with your actual URL
driver.get(url_path)

# Use WebDriverWait to wait for a specific element to be present on the page
wait = WebDriverWait(driver, 20)  # Set a maximum timeout of 20 seconds

try:
    # Wait for the element containing the laptops to be present on the page before proceeding
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'product')]")))

    laptops = driver.find_elements(By.XPATH, "//div[contains(@class, 'product')]")

    data = []
    for laptop in laptops:
        laptop_data = {}

        # Re-locate the laptop element to avoid StaleElementReferenceException
        laptop = driver.find_element(By.XPATH, "//div[contains(@class, 'product')][1]")

        laptop_info = laptop.text.split('\n')
        for info in laptop_info:
            if info.startswith("$"):
                laptop_data["Price"] = info
            elif "GeForce RTX" in info:
                laptop_data["Graphics Card"] = info
            elif "Core" in info:
                laptop_data["Core"] = info.split("Core")[1].strip()

        if laptop_data:
            data.append(laptop_data)

    df = pd.DataFrame(data)
    print(df)

finally:
    driver.quit()
