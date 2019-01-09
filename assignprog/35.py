
tup1=('Monday','Tuesday','Wednesday','Thursday','Friday')

print "Days in a week are=", tup1


tup2=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')


print "Months in a year are=", tup2


print "concatenated tuple output is=",tup1+tup2


tup3=(1,322,43,5,67)

tup4=(10,40,50,60,80)

tup5=(27,63,444,11,0)

print "Tuple 1=", tup3
print "Tuple 2=", tup4
print "Tuple 3=", tup5

if(cmp(tup3,tup4) and cmp(tup4,tup5) > 0):
    print "Tuple 1 is greater among 3"
elif(cmp(tup4,tup5) and cmp(tup4,tup3) > 0):
    print "Tuple 2 is greater among 3"
else:
    print "Tuple 3 is greater among 3"

tup6=list(tup3)
tup6.append(34)

print "Element inserted after typecasting", tuple(tup6)

del tup3[1]
del tup3


