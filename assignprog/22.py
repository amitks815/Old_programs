import math

x=input("Enter the 1st value=:")
y=input("Enter the 2nd value=:")

if(y>1):
    print "Give a value less than or equal to 1"
else:
    print "arc sine of y=",math.asin(y)
    print "arc cosine of y=",math.acos(y)

print "arc tangent of x=",math.atan(x)
print "tangent of x=",math.tan(x)
print "arc tangent 2 of x by y",math.atan2(x,y)
print "sine of x=",math.sin(x)
print "cosine of x=",math.cos(x)
print "hypotenuse of x and y is=",math.hypot(x,y)
print "Radians to Degrees value of x is=",math.degrees(x)
print "Degrees to Radians value for x is=",math.radians(x)

