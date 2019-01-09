##################  Program to print even numbers and skip values 10,20,30,40 and break for value equal to 50 ###########################################

print "Program to print even numbers and skip values 10,20,30,40 and break for 50 using FOR loop"

for i in range(1,101):
	if(i%2==0):
		if(i==50):
			break
		elif(i==10 or i==20 or i==30 or i==40):
			continue
		else: 
			print i,"is even"


print "\n program to print even numbers and skip values 60,70,80 and break for 90 using while loop"

j=1
while(j<101):
	if(j%2==0):
                if(j==90):
                        break
                elif(j==60 or j==70 or j==80):
                        j+=1
			continue
                else: 
                        print j,"is even"
	j+=1
