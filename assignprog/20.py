print "start of part 1"
num=input("Enter the max no. of elements:=")

a=0
b=1

print a
print b 

for i in range(num-2):
	temp=a+b
	a=b
	b=temp
	print temp


print "end of part 1\n "


################## PRINT FIBONACCI UNTIL MAX NUMBER #####################

print "start of part 2"
print "Fibonacci series to be printed less than max number"
num1=input("Enter the max no. of elements=")
a=0
b=1

print a
print b
temp1=0
for i in range(num1-2):
       	if(b<num1): 
		temp1=a+b
        	a=b
       		b=temp1
      		if(temp1>num1):
			break
		else:

			print temp1



print "end of part 2"



