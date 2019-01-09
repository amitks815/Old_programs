dict1={'Name':'Ramakrishna','Age':25}
dict2={'Empid':1234,'Salary':5000}

print "Dict1=",dict1
print "Dict2=",dict2

dict1.update(dict2)
print"output of merger of Dict1 and Dict2=", dict1

dict1['Salary']=5500
dict1['Age']=26

print "updated salary and age values in dictionary =",dict1


dict1['Grade']='B1'

print "Grade inserted in dictionary=",dict1

print "Keys in dictionary are=",dict1.keys(), "\nvalues in dictionary are=",dict1.values()

del dict1['Age']

print "dictionary output after deleting the Age key is=",dict1

