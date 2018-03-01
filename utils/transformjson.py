import json

with open('./output1.json') as startup_data: 
  d = json.load(startup_data)
  for startup in d: 
    startup['city'] = 'Perth'
  out = json.dumps([row for row in d])
  f=open('./output2.json', 'w+')
  f.write(out)