from selenium import webdriver
import time
import pandas as pd

# # https://www.geeksforgeeks.org/get-all-text-of-the-page-using-selenium-in-python/
#
# options = webdriver.ChromeOptions()
#
# driver = webdriver.Chrome(options=options)
#
# # Target URL
# driver.get('https://www.kayak.com/flights/EWR-DEN/2023-05-25/2023-06-03?sort=bestflight_a')
# # To load entire webpage
# time.sleep(15)
#
# text_file = driver.find_element("xpath", "/html/body").text
#
# file = open('kayak.txt', 'w', encoding='utf-8')
#
# file.write(text_file)
#
#
# file.close()
#
#
#
# # Printing the whole body text
# print(text_file)
#
# # Closing the driver
# driver.close()
#
# # time.sleep(5)

df = pd.read_csv('kayak.txt', encoding='utf-8')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'flights'})
print(df)

print(df['flights'].iloc[[379]])

cheapest = df[df["flights"].str.contains("Cheapest")]
print(cheapest)

cheap_index = df.index[df['flights']=='Cheapest'].tolist()
print(cheap_index)
incremented = [x+1 for x in cheap_index]
print(incremented)

list_length = len(incremented)
print(list_length)

# print(df['flights'].iloc[incremented[0]])
# print(df['flights'].iloc[incremented[1]])

# for i in range(0,list_length):
#     print(df['flights'].iloc[incremented[i]])

cheap_list = []

for i in range(0, list_length):
    cheap_item = df['flights'].iloc[incremented[i]]
    print(cheap_item)
    cheap_list.append(cheap_item)
    # print(df['flights'].iloc[incremented[i]])

print(cheap_list)

# df.to_csv('kayak_parsed.csv')

