a = input("Enter 1st element:")
b = input("Enter 2nd element:")
c = input("Enter 3rd element:")
d = input("Enter 4th element:")
e = input("Enter 5th element:")

if (a > b and a < c and a > d):
    print a, "is greater among first4 elements"
    if (a > e):
        print a, "is greater among all 5 elements"
    else:
        print e, "is greater among all 5 elements"
elif (b > c and b > d and b > a):
    print b, "is greater among first 4 elements"
    if (b > e):
        print b, "is greater among all 5 elements"
    else:
        print e, "is greater among all 5 elements"
elif (c > a and c > b and c > d):
    print c, "is greater among first 4 elements"
    if (c > e):
        print c, "is greater among all 5 elements"
    else:
        print e, "is greater among all 5 elements"
else:
    print d, "is greater among first 4 elements"
    if (d > e):
        print d, "is greater among all 5 elements"
    else:
        print e, "is greater among all 5 elements"
