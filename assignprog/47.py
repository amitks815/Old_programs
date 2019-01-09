def extend(tup,list1):

    print " Tuple passed is", tup
    print "List passed is", list1
    tup1=tuple(list1)
    tup2=tup+tup1
    return tup2
 

 


tup=input("Enter elements for a tuple:=")
list1=input("Enter elements for a list:=")

tup2=extend(tup,list1)
print "The output of a tuple extended with a list is=",tup2
   
