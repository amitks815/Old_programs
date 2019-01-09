lower=int(input("print lower number:"))
upper=int(input("print upper number:"))
num=int(input("enter the divisor:"))

for i in range(lower,upper+1):
   if(i%num==0):
       print(i)