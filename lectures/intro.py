'''
class a1:
	# def __init__(self,a1,b1):
	# 	self.a1=a1
	# 	self.b1=b1
	def sum1(self,a,b):
		return a+b
class b1:
	# def __init__(self,a1,b1):
	# 	self.a1=a1
	# 	self.b1=b1
	def sum1(self,a,b):
		return a+b
class c(a1,b1):
	pass
e=c(2,3)
e.sum1()
'''
class a:
	def sum(self,x,y):
		return x+y
class b:
	def sum(self,x,y):
		return x-y

class c(a,b):
	pass

e =c()
print(e.sum(5,4))



