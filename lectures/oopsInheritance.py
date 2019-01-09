class pelican:
	def __init__(self):
		print ("\n __init__\n")
		print ("I am constructor, I initiated by default while creating object on my class")
		print ("Attributes declared here can be accessed through this class")
	def myNames(self):
		print ("\nmyNames\n")
		print ("I am called American White Pelican in America")
		print ("I am called Brown pelican from north to south America")
		print ("I am called Peruvian pelican from Pacific coastal area")

class pelicanAttributes(pelican):		
	def myColours(self):
		print ("\nmyColours\n")
		print ("My colours White, brown, Pink, Black with White, Grey, Greyish-white")
		
	def myFoods(self):
		print ("I eat fish, Amphibians, turtles, crustaceans")


