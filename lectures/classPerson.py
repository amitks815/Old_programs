
class person:
	def __init__(self, age):
		self.name = "Uday"
		self.age = age
		print "I am in constructor", self.age
	def getName(self):
		self.age = 30
		print "Age value in getName method %s " % (self.age)
		return self.name
	def getAge(self):
		return self.age



if __name__ == "__main__":		
	p = person(20)
	print "This is from getAge method : ", p.getAge()
	#print (p.getName())
	#print (p.getAge())
