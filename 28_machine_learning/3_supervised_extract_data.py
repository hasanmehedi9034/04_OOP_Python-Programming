'''
    1. target
    2. data collect
    3. plot cleaning
    4. Model
    5. Predict
'''

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/IPhone'
text = requests.get(url).text.encode('utf8').decode('ascii', 'ignore')
soup = BeautifulSoup(text, 'lxml')

table = soup.find('table', class_='wikitable')
rows = table.findAll('tr')[1 : ]
for row in rows:
    data = row.findAll(['th', 'td'])
    try:
        # print(data[0].a.text.split(' ')[1])
        print(data[-1])
    except:
        pass












