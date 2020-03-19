from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

import csv
from datetime import datetime

import urllib
from bs4 import BeautifulSoup

quote_page = ''

page = urllib.request.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find_all('div', class_='')

# # strip() is used to remove starting and trailing
# name = name_box.innerText().strip()
print(name_box.get_text())

# print(soup.get_text())
