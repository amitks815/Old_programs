"""6.	Create a clock program to display a time based on the given input time,It has to say Good morning, Good afternoon, Good Evening or Good night"""


Time = input("Enter the time in 12hrs format ? ")
amPm = input("Enter the time am or pm ? ")

#if Time >= 4 and Time < 12:
#if Time in range(4,13):
if Time >= 4 and Time < 12 and amPm == 'am':
	print "Good morning"
elif ((Time >=1 and Time < 5) or Time == 12) and ampm=='pm':
	print "Good afternoon"
elif (Time > 5 and Time < 12) and ampm=='pm':
	print "Good evening"
else:
	print "Enter the correct time value in the foramt of 24hs"