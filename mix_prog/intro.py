import re
with open ("hello.txt",'r') as f:
	obj=f.read()

	p=re.match(r'this is',obj)
	print(p)

# 	matches =p.finditer(obj)

# 	for match in matches:
# 		print(match)

# # item =p.findall(obj)
# # print(item)