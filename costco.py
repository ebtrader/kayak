from selenium import webdriver
import time
import pandas as pd

# https://www.geeksforgeeks.org/get-all-text-of-the-page-using-selenium-in-python/

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)

url_path = 'https://www.costco.com/gaming-computers.html?gclid=Cj0KCQjwuNemBhCBARIsADp74QQNsBzfRUh8SyFhYNAOH3WSPMbgh7DL8q3JDsRHTdc9OWc6_Pv3p5IaAvMuEALw_wcB&graphic-card=nvidia-geforce-rtx-3060ti+nvidia-geforce-rtx-4060ti+nvidia-geforce-rtx-3060+nvidia-rtx-4070ti+nvidia-geforce-rtx-3070ti+nvidia-geforce-rtx-3080+nvidia-geforce-rtx-4070+nvidia-geforce-rtx-4080&memory-(ram)=32-gb&deliveryFacetFlag=false&refine=%7C%7CMemory__RAM__attr-32%2BGB%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B3060Ti%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4060Ti%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B3060%7C%7CGraphic_Card_attr-NVIDIA%2BRTX%2B4070Ti%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B3070Ti%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B3080%7C%7CGraphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4070||Graphic_Card_attr-NVIDIA%2BGeForce%2BRTX%2B4080'
# Target URL
driver.get(url_path)

# To load entire webpage
time.sleep(20)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

text_file = driver.find_element("xpath", "/html/body").text


file = open('expedia.txt', 'w', encoding='utf-8')

file.write(text_file)

file.close()

# Printing the whole body text
print(text_file)

# Closing the driver
driver.close()

# time.sleep(5)
#
# df = pd.read_csv('kayak.txt', encoding='utf-8')
# df.reset_index(inplace=True)
# df = df.rename(columns = {'index':'flights'})
# print(df)
#
# print(df['flights'].iloc[[379]])
#
# cheapest = df[df["flights"].str.contains("Cheapest")]
# print(cheapest)
#
# cheap_index = df.index[df['flights']=='Cheapest'].tolist()
# print(cheap_index)
# incremented = [x+1 for x in cheap_index]
# print(incremented)
#
# incremented.append(incremented[1] + 1)
# print(incremented)
#
# list_length = len(incremented)
# print(list_length)
#
# # print(df['flights'].iloc[incremented[0]])
# # print(df['flights'].iloc[incremented[1]])
#
# # for i in range(0,list_length):
# #     print(df['flights'].iloc[incremented[i]])
#
# cheap_list = []
#
# for i in range(0, list_length):
#     cheap_item = df['flights'].iloc[incremented[i]]
#     print(cheap_item)
#     cheap_list.append(cheap_item)
#     # print(df['flights'].iloc[incremented[i]])
#
# print(cheap_list)
#
# best = df[df["flights"].str.contains("Best")]
# print(best)
#
# best_index = df.index[df['flights']=='Best'].tolist()
# print(best_index)
# incremented_best = [x+1 for x in best_index]
# print(incremented_best)
#
# incremented_best.append(incremented_best[1] + 1)
# incremented_best.append(incremented_best[2] + 1)
#
# print(incremented_best)
# del incremented_best[1]
# best_list = []
#
# list_length = len(incremented_best)
# print(list_length)
#
# for i in range(0, list_length):
#     best_item = df['flights'].iloc[incremented_best[i]]
#     print(best_item)
#     best_list.append(best_item)
#     # print(df['flights'].iloc[incremented[i]])
#
# print(best_list)
#
# df.to_csv('kayak_parsed1.csv')
#
