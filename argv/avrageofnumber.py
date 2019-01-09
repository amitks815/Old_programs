list=eval(input("enter the 10 numbers"))
total=0
lenght=len(list)

for i in list:
	total=total+i


avg=total/lenght
print('average of numbers{} is'.format(avg))

count1=0
count2=0
count3=0
for i in list:
	if (i<avg):
		count1=count1+1
		
	
	elif (i>avg):
		count2=count2+1
		
	
	else :
		count3=count3+1
print('count of less then avg:{}\n count of greater then avg:{}\n count of equalthen avg:{}:'.format(count1,count2,count3))

	
	
	