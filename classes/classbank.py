class account:
	def __init__(self,balance,name):
		self.balance=balance
		self.name=name

	def credit(self,deposit):
		self.balance=self.balance + deposit
	def debit(self,withdrawal):
		self.balance=self.balance-withdrawal
	'''def get_balance(self):
		return self.balance
	def get_name(self):
		return self.name
	def set_name(self,name):
		self.name=name'''
customer=account(0,'amit')
print(customer.name,"has balance of",customer.balance)
#print(customer.get_name(),"has balance of",customer.get_balance())
customer.credit(2000)
print(customer.name,"has balance after deposit",customer.balance)
#print(customer.get_name(),"has balance after deposit",customer.get_balance())
customer.debit(100)
print(customer.name,"has balance after withdrawal",customer.balance)
#print(customer.get_name(),"has balance after withdrawal",customer.get_balance())
customer.name='amit kumar'
#customer.set_name('amit kumar')
print(customer.name,"has balance of",customer.balance)
#print(customer.get_name(),"has balance of",customer.get_balance())