import pandas as pd
from bs4 import BeautifulSoup
#import requests library
import requests

# hhttps://www.pylenin.com/blogs/python-beautiful-soup/

#the website URL
url_link = "https://en.wikipedia.org/wiki/List_of_LGBT_characters_in_modern_written_fiction"
result = requests.get(url_link).text
doc = BeautifulSoup(result, "html.parser")

all_tables = doc.find_all('table')
# print(all_tables)
# print(len(all_tables))


# print(doc.prettify())

required_table=doc.find('table', class_="wikitable sortable")
# print(my_table)
headers = [header.text.strip() for header in required_table.find_all('th')]
print(headers)

rows = []

# Find all `tr` tags
data_rows = required_table.find_all('tr')

for row in data_rows:
    value = row.find_all('td')
    beautified_value = [ele.text.strip() for ele in value]
    # Remove data arrays that are empty
    if len(beautified_value) == 0:
        continue
    rows.append(beautified_value)

print(rows)

df = pd.DataFrame(rows, columns=headers)
print(df)
df.to_csv(('lqbtq.csv'))



#
# th_tags = my_table.find_all('th')
# names = []
# for elem in th_tags:
#   #finding the < a > tag
#     a_links = elem.find_all("a")
# #getting the text inside the < a > tag
#     for i in a_links:
#         names.append(i.string)
# print(names)
# #
# # final_list = names[9: ]
# # states = []
# # for str in final_list:
# #     if len(str) > 3:
# #         states.append(str)
# # print(states)
# #
# # divs = my_table.find_all("div")
# # pop = []
# # for i in divs:
# #   pop.append(i.string)
# # print(pop)
# #
# # pop_final = []
# # for i in pop:
# #   if len(i) > 3:
# #     pop_final.append(i)
# # print(pop_final)
# #
# # import pandas as pd
# #
# # df = pd.DataFrame()
# #
# # df['state'] = states
# # df['population'] = pop_final
# #
# # print(df)