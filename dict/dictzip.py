l1=['a','b','c','d']
l2=['w','x','y','z']

z1=zip(l1,l2)

dict_zip=zip(l1,l2)
print(list(z1))
print(dict(dict_zip))

for l1,l2 in zip(l1,l2):
	print(l1,l2)