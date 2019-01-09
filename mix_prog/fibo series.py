#num=eval(input("Enter the max no. of elements:="))
def fibo(num):
	a=0
	b=1

	print (a)
	print (b) 

	for i in range(num-2):
		temp=a+b
		a=b
		b=temp
	#return temp 
		print (temp)
num=eval(input("enter the sequence upto:"))
fibo(num)
