list1=input("Enter list1 elements:")
list2=input("Enter list2 elements:")
list3=input("Enter list3 elements:")

print"Length of list1 is=",len(list1)
print"Length of list2 is=",len(list2)
print"Length of list3 is=",len(list3)

print "Maximum value in list1 =",max(list1),"Minimum value in list1 =",min(list1)
print "Maximum value in list2 =",max(list2),"Minimum value in list2 =",min(list2)
print "Maximum value in list3 =",max(list3),"Minimum value in list3 =",min(list3)

if(cmp(list1,list2) and cmp(list1,list3) >0):
	print list1,"is greatest among the 3"
elif(cmp(list2,list3) and cmp(list2,list1) >0):
	print list2,"is greatest among the 3"
else:
	print list3,"is greatest among the 3"

del list1[0];del list1[-1];del list2[0];del list2[-1]; del list3[0]; del list3[
-1]

print "New list1 =", list1,"\n New list2=",list2,"\n New list3=", list3

