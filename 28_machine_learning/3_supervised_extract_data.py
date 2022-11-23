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
import csv

url = 'https://en.wikipedia.org/wiki/IPhone'
text = requests.get(url).text.encode('utf8').decode('ascii', 'ignore')
soup = BeautifulSoup(text, 'lxml')

table = soup.find('table', class_='wikitable')
rows = table.findAll('tr')[1 : ]

iphone_price_dict = {}

for row in rows:
    data = row.findAll(['th', 'td'])
    try:
        version_text = (data[0].a.text.split(' ')[1])
        version = re.sub(r"\D", "", version_text)
        
        price_text = (data[-1].text.split('/')[-1])
        price = int(re.sub(r"\D", "", price_text))
        
        if version and price > 100:
            iphone_price_dict[version] = price
    except:
        pass

print(iphone_price_dict)
csv_field = ['version', 'price']

with open('iphone_price.csv', 'w', newline="") as csv_file:
    csv_writter = csv.writer(csv_file)
    # csv_writter.writerows(csv_field)
    
    for key, value in iphone_price_dict.items():
        csv_writter.writerow([key, value]) 
csv_file.close()    









