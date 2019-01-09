def sum(x, y):
	print(x+y)
	def do_it():
		return x+y
	return do_it 
a = sum(1, 3)