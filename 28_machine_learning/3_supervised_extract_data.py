'''
    1. target
    2. data collect
    3. plot cleaning
    4. Model
    5. Predict
'''

import requests
from bs4 import BeautifulSoup
import re

url = 'https://en.wikipedia.org/wiki/IPhone'
text = requests.get(url).text.encode('utf8').decode('ascii', 'ignore')
soup = BeautifulSoup(text, 'lxml')

table = soup.find('table', class_='wikitable')
rows = table.findAll('tr')[1 : ]
for row in rows:
    data = row.findAll(['th', 'td'])
    try:
        version_text = (data[0].a.text.split(' ')[1])
        version = re.sub(r"\D", "", version_text)
        
        price_text = (data[-1].text.split('/')[-1])
        price = re.sub(r"\D", "", price_text)
        print(version, price)
    except:
        pass












