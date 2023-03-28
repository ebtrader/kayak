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
print(all_tables)
