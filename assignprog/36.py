
tup1=(10,20,30,40,50)

tup2=('start','hi','iam','ur','voice','over')

print "Tuple 1 is ",tup1
print "Tuple 2 is", tup2
print "Length of tuple1 is", len(tup1), "\nLength of tuple2 is ", len(tup2)
print "Maximum element in tuple1 is", max(tup1)
print "Minimum element in tuple 2 is", min(tup2)

if(cmp(tup1,tup2)>0):
    print "Tuple1 is greater"
else:
    print "Tuple2 is greater"

list=[1,2,3,4,5]
print "list typecasted to tuple=", tuple(list)
