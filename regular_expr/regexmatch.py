import re

from re import split
# with open('hello.txt','r') as f:
# 		content=f.read()
# 	#pattern=re.compile(r'')
# 	pattern=re.compile(r'[a-zA-z0-9.-]+@[a-zA-z0-9-]+.[a-zA-Z0-9-]+')
# 	matches=pattern.finditer(content)
# 	for match in matches:
# 	print(match.group(0))

# # str1='is here amit'
# # str2=re.search('amit$',str1)
# # print(str2)

# # tup1=('amit',2.23,77.23)
# # print(tup1)


#split method 
# '\W+' denotes Non-Alphanumeric Characters or group of characters
# Upon finding ',' or whitespace ' ', the split(), splits the string from that point
print(split('\W+', 'Words, words , Words'))

#re.split(pattern,pattern, string, maxsplit=0, flags=0)
print(split('\W+', "Word's words Words"))

# re.sub(pattern, repl, string, count=0, flags=0)

print(re.sub('ub', '~*' , 'Subject has Uber booked already', flags = re.IGNORECASE))
# re.sub(pattern, repl, string, count=0, flags=0)
# it retuen value in tuple 

print(re.subn('ub', '~*' , 'Subject has Uber booked already'))
t = re.subn('ub', '~*' , 'Subject has Uber booked already', flags = re.IGNORECASE)
print(t)
print(len(t))
 
# This will give same output as sub() would have 
print(t[0])
