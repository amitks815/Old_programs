class employee():
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

emp1=employee('amit','kumar',1000000)
print(emp1.fullname())
#print(employee.fullname(emp1))