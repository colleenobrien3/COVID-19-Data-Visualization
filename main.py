from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

import csv
from datetime import datetime

import urllib
from bs4 import BeautifulSoup

quote_page = 'https://forecast.weather.gov/MapClick.php?x=161&y=208&site=phi&zmx=&zmy=&map_x=161&map_y=208#.XnKvo5NKjGI'

page = urllib.request.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find(id='seven-day-forecast-list')

# # strip() is used to remove starting and trailing
# name = name_box.innerText().strip()
print(name_box.get_text())

# print(soup.get_text())
