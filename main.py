from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

import csv
from datetime import datetime

import urllib
from bs4 import BeautifulSoup

quote_page = 'https://www.worldometers.info/coronavirus/country/us/'

page = urllib.request.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find_all('td')

# # strip() is used to remove starting and trailing
# name = name_box.innerText().strip()

for i in name_box:
    print(i.get_text())

# print(soup.get_text())
