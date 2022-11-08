import csv

with open('./my_friends.csv', 'r') as f:
    lines = csv.reader(f)
    header = next(lines)
    
    for line in lines:
        print(line)
        
    print(header)