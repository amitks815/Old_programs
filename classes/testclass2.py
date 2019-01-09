class createaccount:
	def __init__(self,customer_name,customer_balance):
		self.name=customer_name
		self.balance=customer_balance
	
	def customer_name(self):
		return self.name

	def customer_balance(self):
		return self.balance

account_holder=createaccount("amit kumar",10000)
print("name of customer is:",account_holder.customer_name())
print("balance of accountid :",account_holder.customer_balance())