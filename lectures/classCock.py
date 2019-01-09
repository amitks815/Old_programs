#Class a blue print of object. Or its a name space for collection of similar function
#class is a key word to declare the Class
#Identifiers called as a attributes and function called as a Method

class cock:
	def chicken():
		print ("i am chicken")
	def egg():
		color = "white"
		print ("i am egg")

class pelican:
	def __init__(self):
		print ("I am constructor, I initiated by default while creating object on my class")
		print ("Attributes declared here can be accessed through this class\n")
		print (self)
	def myNames(self):
		print ("I am called American White Pelican in America")
		print ("I am called Brown pelican from north to south America")
		print ("I am called Peruvian pelican from Pacific coastal area\n")
		
	def myColours(self):
		print ("My colours White, brown, Pink, Black with White, Grey, Greyish-white\n")
		print (self)
	def myFoods(self):
		print ("I eat fish, Amphibians, turtles, crustaceans\n")
