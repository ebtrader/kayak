from selenium import webdriver
import pandas as pd
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# original = https://www.costco.com/laptops.html?graphic-card=nvidia-geforce-rtx-3050+nvidia-geforce-rtx-3050ti+nvidia-geforce-rtx-3070ti+nvidia-geforce-rtx-4050+nvidia-geforce-rtx-4060+nvidia-geforce-rtx-4070+nvidia-geforce-rtx-4080&memory-(ram)=32-gb+64-gb&deliveryFacetFlag=false&refine=%7C%7CMemory__RAM__attr-32%2BGB%7C%7CMemory__RAM__attr-64%2BGB%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B3050%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B3050Ti%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B3070Ti%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4050%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4060%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4070||Graphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4080

url_path = 'https://www.costco.com/laptops.html?graphic-card=nvidia-geforce-rtx-3050+nvidia-geforce-rtx-3050ti+' \
           'nvidia-geforce-rtx-3070ti+nvidia-geforce-rtx-4050+nvidia-geforce-rtx-4060+nvidia-geforce-rtx-4070+' \
           'nvidia-geforce-rtx-4080&memory-(ram)=32-gb+64-gb&deliveryFacetFlag=false&refine=%7C%7CMemory__' \
           'RAM__attr-32%2BGB%7C%7CMemory__RAM__attr-64%2BGB%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B3050%7C%7CGraphic_Card_' \
           'attr-NVIDIA%2BGeForce%2BRTX%2B3050Ti%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B3070Ti%7C%7CGraphic_Card_' \
           'attr-NVIDIA%2BGeForce%2BRTX%2B4050%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4060%7C%7CGraphic_Card_' \
           'attr-NVIDIA%2BGeForce%2BRTX%2B4070||Graphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4080'   # Update this with your actual URL
driver.get(url_path)

# Wait for the page to load completely
driver.implicitly_wait(10)  # Adjust the wait time as needed

data = []
while True:
    laptop_elements = driver.find_elements("xpath", "//div[contains(@class, 'product')]")

    for laptop_element in laptop_elements:
        laptop_data = {}

        try:
            laptop_text = laptop_element.text

            lines = laptop_text.split('\n')
            for line in lines:
                if line.startswith("$"):
                    laptop_data["Price"] = line
                elif "GeForce RTX" in line:
                    laptop_data["Graphics Card"] = line
                elif "Core" in line:
                    laptop_data["Core"] = line.split("Core")[1].strip()

            if laptop_data:
                data.append(laptop_data)
        except Exception as e:
            print("Error processing laptop element:", e)

    try:
        next_button = driver.find_element("xpath", "//button[@aria-label='Next']")
        if next_button.is_enabled():
            next_button.click()
            time.sleep(2)  # Add a short delay to allow the page to load
        else:
            break
    except Exception as e:
        print("No more pages available:", e)
        break

df = pd.DataFrame(data)
print(df)
df.to_csv('costco.csv', index=False)

driver.quit()
