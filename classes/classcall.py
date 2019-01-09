class robot:
	def __init__(self,name):
		print(name  +' '+'has been created')

	def __del__(self):
		print('robot has been destroyed')

x=robot('amit')
del x
