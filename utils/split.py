import json

with open('./output2.json') as startup_data: 
  d = json.load(startup_data)
  for startup in d: 
    text = startup['description']
    founded, desc = text.split('\n')
    [ text ,foundedYear] = founded.split(':')
    startup['description'] = desc.lstrip()
    startup['founded'] = foundedYear
    
  out = json.dumps([row for row in d])
  f=open('./output3.json', 'w+')
  f.write(out)