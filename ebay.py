from selenium import webdriver
import time
import pandas as pd

# https://www.geeksforgeeks.org/get-all-text-of-the-page-using-selenium-in-python/

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)

url_path = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=snowboard+boots+size+8&_sacat=0'
# Target URL
driver.get(url_path)
# To load entire webpage
time.sleep(15)

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
