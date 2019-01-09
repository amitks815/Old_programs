try:
	fo=open("hello.txt")
	if fo.name=='hello.txt':
		raise Exception
	#a = something
except FileNotFoundError as e:#system defind error message for (AS e)
	print(e)
except Exception:
	print('Error!') 
else:
	obj=fo.read()
	print(obj)	
finally:
	fo.close()
	print('*********done with program*************')

