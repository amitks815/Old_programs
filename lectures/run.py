import re

fh = open("ipconfig")

for line in fh:
	#print line.strip()
	#if re.search('[0-9][0-9][0-9][0-9]', line):
	#if re.search('[0-9]{3,5}', line):
	#if re.search('\d\d\d\d', line):
	#if re.search('\d{4}', line):
		#m = re.search('(\d{4})', line)
		#print m.group()
	#if re.search('\d{3}', line):
	#	m = re.findall('(\d{3})', line)
	#	print m
	#if re.search('[basavaraj]', line):
	#if re.search('(basavaraj)', line):
	#	print line.strip()

	#inet 192.168.1.13 netmask 0xffffff00 broadcast 192.168.1.255
	if re.search("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}.*broadcast", line):
		print line.strip()
fh.close()
'''

str1 = "Mayer is a very common Name"
str2 = "He is called Mayer but he isn't German."

print(re.match("Mayer", str1))
print(re.match("Mayer", str2))

print "--------------------"

print(re.search("Mayer", str1))
print(re.search("Mayer", str2))

print "--------------------"
print(re.search("^Mayer", str1))
print(re.search("^Mayer", str2))

print "--------------------"

print(re.search("e$", str1))
print(re.search("e$", str2))

str1 = "Mayer is a very common Name"
str2 = "He is called gentle man but he isn't German."

var1 = str2 + "\n" + str1
print (var1)

print(re.search("^Mayer", var1))
print(re.search("^Mayer", var1, re.MULTILINE))
print(re.search("^Mayer", var1, re.M))
print(re.match("^Mayer", var1, re.M))
'''

#print(re.search(".txt$","I like Python.txt"))
#print(re.search(".txt$","txt"))
#print(re.search(".txt$","Atxt"))
#print(re.search(".txt$","I like Pythontxt"))
#print(re.search("\.txt$","I like Python.txt"))

#print(re.search("....","abc"))

#print(re.search("python","I like Python"))
#print(re.search("python","I like Python", re.I))

'''
print re.search("a", "I am Python")
print re.search("a*", "I am Python")
print re.search("a*", "I m Python")

print "==============="
print re.search("a+", "I am Python")
print re.search("[0-9]+", "I m2 Python")

print re.search("Python|Perl", "I am Perl")
print re.search("Python|Perl", "I am Python")
print re.search("Python|Perl", "I am java")


pattern = re.compile('(Python|Perl)')

print re.sub(pattern, "#######", "I am Perl")

'''






