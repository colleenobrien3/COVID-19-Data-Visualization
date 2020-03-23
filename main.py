

import json
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

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
    for j in range(8):
        newObj.append(whole.pop(0))
    newerObj.append(newObj)
    newObj = []

f = open('dataFile.py', 'w')
f.write(str(newerObj))
f.close()


data = []
for i in newerObj:
    data.append({
        'name': i[0],
        'total_cases': i[1],
        'new_cases': (i[2]),
        'total_deaths': (i[3]),
        'new_deaths': i[4],
        'total_recovered': i[5],
        'active_cases': i[6],
        'source': i[7]
    })


with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)


# print(newerObj)


# -------------------------------
