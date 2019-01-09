dict1={'name':'sam','age':33,'Gender':'Male'}
dict2={'name':'bill','age':44,'Gender':'Female','Id':1223}
dict3={'name':'beck','age':22,'Gender':'Male','Id':2223,'Place':'US'}

print "Dict 1=",dict1
print "Dict 2=",dict2
print "Dict 3=",dict3

if(cmp(dict1,dict2) and cmp(dict1,dict3) > 0):
    print "Dict1 is greater among 3"
elif(cmp(dict2,dict3) and cmp(dict2,dict1) >0):
    print "Dict2 is greater among 3"
else:
    print "Dict3 is greater among 3"

print "Length of dict1 is ", len(dict1)
print "Length of dict2 is", len(dict2)
print "Length of dict3 is", len(dict3)

str1=str(dict1)
str2=str(dict2)
str3=str(dict3)



print "concatenated string after typecasting=",str1+str2+str3
