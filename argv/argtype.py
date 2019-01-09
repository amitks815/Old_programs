def getUserName(fn,ln):
	name = fn + ' ' + ln
	return name
	
print (getUserName('Sachin','Tendulkar'))
print (getUserName('Tendulkar','Sachin'))
print (getUserName(fn='Sachin',ln='Tendulkar'))
print (getUserName(ln='Tendulkar',fn='Sachin'))
print (getUserName('Tendulkar',ln='Sachin'))