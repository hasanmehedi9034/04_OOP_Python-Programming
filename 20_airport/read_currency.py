import csv

with open('./data/currencyrates.csv', 'r') as f:
    lines = csv.reader(f)
    
    for line in lines:
        if 'Bangladesh' in line[0]:
            print(f'{float(line[3]) * 50} {line[1]}')
