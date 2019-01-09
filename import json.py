import json

#print(dir(json))

with open('example_2.json','r') as obj:
    f=obj.read()
    data=json.load(obj)
    print(data)
    #print(f)