from bs4 import BeautifulSoup
#import requests library
import requests

# https://www.topcoder.com/thrive/articles/web-scraping-with-beautiful-soup

#the website URL
url_link = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
result = requests.get(url_link).text
doc = BeautifulSoup(result, "html.parser")

# print(doc.prettify())

# res = doc.find(id = "content")
# print(res)

# heading = res.find(class_ = "firstHeading")
# print(heading)
#
# print(heading.text)

# for ele in res:
#     print(res.find("h2"))

import re

# for str in doc.find_all(text = re.compile("1788")):
#     print(str)

my_table=doc.find('table', class_='wikitable sortable plainrowheaders')

th_tags = my_table.find_all('th')
names = []
for elem in th_tags:
  #finding the < a > tag
    a_links = elem.find_all("a")
#getting the text inside the < a > tag
    for i in a_links:
        names.append(i.string)
print(names)

final_list = names[9: ]
states = []
for str in final_list:
    if len(str) > 3:
        states.append(str)
print(states)

divs = my_table.find_all("div")
pop = []
for i in divs:
  pop.append(i.string)
print(pop)

pop_final = []
for i in pop:
  if len(i) > 3:
    pop_final.append(i)
print(pop_final)

import pandas as pd

df = pd.DataFrame()

df['state'] = states
df['population'] = pop_final

print(df)