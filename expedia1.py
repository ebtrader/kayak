from selenium import webdriver
import time
import pandas as pd

# https://www.geeksforgeeks.org/get-all-text-of-the-page-using-selenium-in-python/

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)

# Target URL
driver.get('https://www.expedia.com/Hotel-Search?adults=2&d1=2023-05-03&d2=2023-05-08&'
           'destination=Grace%20Bay%2C%20Providenciales%2C%20Providenciales%2C%20Turks%20and%20Caicos&'
           'endDate=2023-05-08&latLong=21.799715%2C-72.168269&regionId=55041&rooms=1&semdtl=&sort=RECOMMENDED&'
           'startDate=2023-05-03&theme=&useRewards=false&userIntent=')
# To load entire webpage
time.sleep(15)

# text_file = driver.find_element("xpath", "/html/body").text


parser = driver.find_element("xpath", "///script[@id='cachedResultsJson']//").text

# json_data_xpath = parser.xpath("//script[@id='cachedResultsJson']//text()")

# hotels = driver.find_element('xpath', './/h3[@data-stid="content-hotel-title"]').text
#
    # review = hotel.xpath('string(.//div[@data-stid="content-hotel-review-info"]/span/span[1])').get()
    # price = hotel.xpath('.//span[@data-stid="price-lockup-text"]/text()').get()
    # hotel_name = hotel.xpath('.//h3[@data-stid="content-hotel-title"]/text()').get()
    # location = hotel.xpath('.//div[@data-test-id="content-hotel-neighborhood"]/text()').get()


# file = open('expedia.txt', 'w', encoding='utf-8')
#
# file.write(text_file)
#
#
# file.close()



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
