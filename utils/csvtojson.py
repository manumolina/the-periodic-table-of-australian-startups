import csv 
import json
f = open('./csv/Perth.csv', 'rU')
reader = csv.DictReader(f, fieldnames=('name', 'description'))

out = json.dumps([row for row in reader])

f=open('./output1.json', 'w+')
f.write(out)
