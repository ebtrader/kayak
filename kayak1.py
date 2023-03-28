import requests

from bs4 import BeautifulSoup

url = 'https://www.kayak.com/flights/SEL-LON/2023-05-31?sort=bestflight_a'
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,pl;q=0.8",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

departure_times = soup.find_all('span', {'class': 'depart-time base-time'})

for _time in departure_times:
    print(_time.text)