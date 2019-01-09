dict={'name':"amit",'age':25,"id":'123re'}
print(dict['name'])
dict["school"]='DPS'
print(dict)
dict["school"]='SSM'
#del (dict['school'])
#dict.clear()
dict2=dict.copy()
print(dict2)
print(len(dict))

#fromkeys

seq=('name','10','group')
dict=dict.fromkeys(seq)
print(dict)
dict=dict.fromkeys(seq,10)
print(dict)

#getkey

dict={'name':"amit",'age':26}

print(dict.get('name'))
print(dict.get('sex'))

print(dict)

#has_key()
'''dict = {'Name': 'Zara', 'Age': 7}

print ("Value : %s" %  dict.has_key('Age'))
print ("Value : %s" %  dict.has_key('Sex'))'''

#items
#dict1={'name':"amit",'age':26}
#print(dict.item())


#update
dict.update(dict2)
print(dict)

#values

print ("Values : ",  list(dict.values()))


#keys
print(dict.keys())
