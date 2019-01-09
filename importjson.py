import json

#print(dir(json))

with open('guest_card.json','r') as obj:
    
    data=json.load(obj)

for val in data:
    	#print (val['id'],val['first_seen'])
	del (val['shown_unit'],val['marketing_source'])
	print(val)
with open ('guest_card_mod.json','w') as f:

	json.dump(data,f) 


    #print(data)
    #print(f)