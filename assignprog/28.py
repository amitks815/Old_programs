print "Program to check the vowels in a given string"

str=raw_input("Enter a string:")
count=0
a=0
i=0
e=0
o=0
u=0
for sear in str:
	if(sear=='a'):
		a=a+1
	elif(sear=='e'):
		e=e+1
	elif(sear=='o'):
		o=o+1
	elif(sear=='i'):
		i=i+1
	elif(sear=='u'):
		u=u+1
		
print "vowel a =",a,"vowel e =",e,"vowel i =",i,"vowel o =",o,"vowel u =",u
print "Total no. of vowels is=",a+e+i+o+u
