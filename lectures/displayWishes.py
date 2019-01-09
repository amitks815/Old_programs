#Create a clock program to display a time based on the given input time,
#	It has to say Good morning, Good afternoon, Good Evening or Good night

from sys import argv
#Time = 13
#Time = int(argv[1])
#Time = input("Enter the time (8,13,18)? ")
#Time = input("Enter the time(24hrs format)? ")
#12hr format

Time = input("Enter the time in 12hrs format ? ")
amPm = input("Enter the time am or pm ? ")

#if Time >= 4 and Time < 12:
#if Time in range(4,13):
if Time >= 4 and Time < 12 and amPm == 'am':
	print "Good morning"
elif Time == 13:
	print "Good afternoon"
elif Time == 18:
	print "Good evening"
else:
	print "Enter the correct time value in the foramt of 24hs"


input
condition
if cond :
	print "True"
elif cond:
	print "True"

print
