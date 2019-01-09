import calendar

cal1=calendar.calendar(2016,w=10)

print "calendar 2016 with 10 char width:", cal1

cal2=calendar.leapdays(1980,2025)

print "Leapdays between years 1980 to 2025=", cal2

year1=input("Enter any year for calculation:=")

if(calendar.isleap(year1)):
    print year1,"is a leap year"
else:
    print year1,"is not a leap year"

mon=input("Enter any value for a month:=")

cal3=calendar.month(2016,mon)
print cal3,"is the",mon,"th month in 2016"
