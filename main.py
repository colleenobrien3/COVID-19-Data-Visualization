from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

import csv
from datetime import datetime

import urllib
from bs4 import BeautifulSoup

# quote_page = 'https://www.worldometers.info/coronavirus/country/us/'

# page = urllib.request.urlopen(quote_page)

# soup = BeautifulSoup(page, 'html.parser')

# name_box = soup.find_all('td')

# # # strip() is used to remove starting and trailing
# # name = name_box.innerText().strip()

# for i in name_box:
#     print(''.join(i.get_text().strip()))


# ------------------------

quote_page = 'https://www.worldometers.info/coronavirus/country/us/'
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find_all('td')

whole = []

for i in name_box:
    whole.append(''.join(i.get_text().strip()))

newObj = []
newerObj = []

for i in range(50):
    for j in range(7):
        newObj.append(whole.pop(0))
    newerObj.append(newObj)
    newObj = []

print(newerObj)
