import json

with open('./output3.json') as startup_data:
  with open('./output.html', 'w+') as f:
    
    d = json.load(startup_data)
    for startup in d: 
      name = startup['name']
      city = startup['city']
      founded = startup['founded']
      description = startup['description']
      
      htmlString= "\
      <div class=\"startup-detail-container %s\"> \n\
        <div class=\"startup-em\"></div>\n\
        <div class=\"name\">%s</div>\n\
        <div class=\"description\">%s</div>\n\
      </div>\n\n"%(city.lower(), name, description)
  
      f.write(htmlString.encode('utf-8'))