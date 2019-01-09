f_name=['amit','atul','deepak','ram']
l_name=['kumar','singh','sharma','bhagat']

# dictinonary comprehansive

mydict={f_name:l_name for f_name,l_name in zip(f_name,l_name) }
print(mydict)
