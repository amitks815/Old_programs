## Global vs. Local variable declaration
b = 10
def globalVsLocalVars():
	print "Inside the function : ", b

globalVsLocalVars()
print "Outside the function : ", b

b = 10
def globalVsLocalVars():
	#global b
	print "Inside the function(global declaration) : ", b
	b = 100
	print "Inside the function(local declaration) : ",b 

globalVsLocalVars()
print "Outside the function : ", b

b = 10
def globalVsLocalVars(b):
	print "Inside the function : ", b
	b = 100
	print "Inside the function(local declaration) : ", b
globalVsLocalVars(b)
print "Outside the function : ", b
