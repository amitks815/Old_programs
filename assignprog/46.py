def biggest(a,b,c,d):
    if(a>b and a<c and a>d):
        print a,"is greater among 4"
    elif(b>c and b>d and b>a):
        print b,"is greater among 4"
    elif(c>a and c>b and c>d):
        print c,"is greater among 4"
    else:
        print d,"is greater among 4"
    return


num1=input("Enter 1st number=")
num2=input("Enter 2nd number=")
num3=input("Enter 3rd number=")
num4=input("Enter 4th number=")

print"\n ********** printing the output with required arguments**********"

biggest(num1,num2,num3,num4)

def biggest1(i,j=10,k=20,l=55):
    if(i>j and i>k and i>l):
        print i,"is greater among 4"
    elif(j>i and j>k and j>l):
        print j,"is greater among 4"
    elif(k>i and k>j and k>l):
        print k,"is greater among 4"
    else:
        print l,"is greater among 4"
    return

print"\n************printing the output with default arguments**********"

biggest1(127)

