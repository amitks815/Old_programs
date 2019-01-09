class class_demo:
	def meth(self):
		print("welcome to the class")

	@classmethod
	def class_method(cls):
		print(cls().meth())
		print("This is class method")

	@staticmethod
	def static_method():
		

class_demo.class_method()
myinst_1=class_demo()
print (type(class_demo))
myinst_1.meth()
