print("import my module from file")

test='this is module calling'

def find_index(to_search,target):
	for i,value in enumerate(to_search):
		if value==target:
			return 1
	else :
		return -1
