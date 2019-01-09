#Regular expression is a language itself
#Regular expression is a more powerful text processing tool. It can be a very simple to complex pattern.
#Its implemented in Python is using 're' module
## Regular Expression operator

'''
Regular expression starts searching or matching from left to right in string, when it matches the pattern it ends the pattern search. 

. -> In default mode it matches any single character till the new line character(except new line character)
^ -> It matches starting of the string/line(caret)
$ -> It mtches end of the string/line
| -> RE OR operator

#Predefined character classes
(abc) - It matches 'abc' word
[abc] - It matches any one of character a or b or c
\d - Matches any single digit
[0-9] - Matches any single digit
\D - Matches any non digit character 
[^0-9] - Matches any non digit character 
\s - Matches any white space character
[\t\n\r\v] - Matches any white space character
\S - Matches any non white space character
[^\t\n\r\v] - Matches any non white space character
\w - Matches any alphanumeric character
[a-zA-Z0-9_] - Matches any alphanumeric character
\W - Matches any non alphanumeric character
[^a-zA-Z0-9_] - Matches any non alphanumeric character
\b	Matches the empty string, but only at the start or end of a word. So \b matches any empty string between a \W and a \w character and also between a \w and a \W character.(For example, r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3')
\B	Matches the empty string, but not at the start or end of a word. \B is the complement, i.e empty strings between \W and \W or empty strings between \w and \w. (r'py\B' matches 'python', 'py3', 'py2', but not 'py', 'py.', or 'py!'. \B is just the opposite of \b)
\ -> Matches a literal backslash(Suppress the regular expression behaviour).

Quantifiers:
? - Matches preceding character or expression 0 or 1 time(optional)
* - Matches preceding character or expression 0(optional) or more times
+ - Matches preceding character or expression 1 or more times
{m,n} - Matches minimum m char to maximum n characters
{m} - Matches exactly m character
{m,} - Matches minimum m character to maximum
{,n} - Matches minimum 0 to maximum n character


match - never checks anything but the beginning of the string for a match.

re.match(<pattern>, <input>, [<mode>])

search - Search will search from starting of the line or string to till the new line character
findall

re.search(<pattern>, <input>, [<mode>])

obj.replace(<Search patern>,<Replace pattern>)

mode:

re.I or re.IGNORECASE --> Makes the regular expression case-insensitive
re.M or re.MULTILINE --> will match at the beginning and at the end of each line and not just at the beginning and the end of the string
'''

import re

x = re.search("cat","A cat and a rat can't be friends.")
print(x)
x = re.search("cow","A cat and a rat can't be friends.")
print(x)


str1 = "Mayer is a very common Name"
str2 = "He is called Mayer but he isn't German."

print(re.match("Mayer", str1))
print(re.match("Mayer", str2))

print(re.search("^Mayer", str1))
print(re.search("^Mayer", str2))

str1 = "Mayer is a very common Name"
str2 = "He is called Meyer but he isn't German."

print(re.search("M[ae]yer", str1))#Mayer
print(re.search("M[ae]yer", str2))#Meyer 

print(re.search("M[ae][iy]er", str1))#Mayer, Meyer, Maier, Meier
print(re.search("M[ae][iy]er", str2))#Mayer, Meyer, Maier, Meier

str1 = "Mayer is a very common Name"
str2 = "He is called gentle man but he isn't German."

var1 = str2 + "\n" + str1
print (var1)

"""
output of
var1 = '''He is called gentle man but he isn't German.
Mayer is a very common Name'''
"""
print(re.search("^Mayer", var1))
print(re.search("^Mayer", var1, re.MULTILINE))
print(re.search("^Mayer", var1, re.M))
print(re.match("^Mayer", var1, re.M))


print(re.search("txt$","I like Python.txt"))

print(re.search(".txt$","I like Pythontxt"))
print(re.search(".txt$","I like Pythoxtxt"))
print(re.search(".txt$","I like Pythoatxt"))
print(re.search(".txt$","I like Python txt"))
print(re.search(".txt$","I like Python*txt"))
print(re.search(".txt$","I like Python.txt"))

print(re.search(".txt$","I like Python.txt"))
print(re.search("\.txt$","I like Pythontxt"))
print(re.search("\.txt$","I like Python.txt"))
print(re.search("Python$","I like Python and Perl."))
print(re.search("Python\.$","I like Python.\nSome prefer Java or Perl."))
print(re.search("Python\.$","I like Python.\nSome prefer Java or Perl.", re.M))

print(re.search("python","I like Python"))
print(re.search("Python","I like Python"))
print(re.search("python","I like Python", re.I))

print "\n* operator\n"
mo = re.search("a", "I am Python")
print (mo)
mo = re.search("a*", "I am Python")
print (mo)
mo = re.search("a*", "I m Python")
print (mo)

print "\n+ operator\n"
mo = re.search("a+", "I am Python")
print (mo)
mo = re.search("a+", "I m Python")
print (mo)

print "\n? operator\n"
mo = re.search("a?", "I am Python")
print (mo)
mo = re.search("a?", "I m Python")
print (mo)

mo = re.search("[0-9]*", "Customer number: 232454, Date: February 12, 2011")
print (mo)
mo = re.search("[0-9]*", "Customer number: ABC, Date: Month, date, year")
print (mo)

mo = re.search("[0-9]+", "Customer number: 232454, Date: February 12, 2011")
print (mo)
mo = re.search("[0-9]+", "Customer number: ABC, Date: Month, date, year")
print (mo)

mo = re.search("[0-9]?", "Customer number: 232454, Date: February 12, 2011")
print (mo)
mo = re.search("[0-9]?", "Customer number: ABC, Date: Month, date, year")
print (mo)

mo = re.search("dh?andapani", "dhandapani")
print (mo)
mo = re.search("dh?andapani", "dandapani")
print (mo)

mo = re.search("[0-9]+", "Customer number:  232454, Date: February 12, 2011")
print (mo.group())
print (mo.span())
print (mo.start())
print (mo.end())
print (mo.span()[0])
print (mo.span()[1])

mo = re.findall("[0-9]+", "Customer number:  232454, Date: February 12, 2011")
print (mo)

mo = re.search("(number)", "Customer number: 232454 Date: February 12 2011")
print (mo)
mo = re.search("(number)", "Customer nomber: 232454 Date: February 12 2011")
print (mo)

mo = re.search("([0-9]+).*: (.*)", "Customer number: 232454 Date: February 12 2011")
print (mo.group())
print (mo.group(1))
print (mo.group(2))
print (mo.group(1,2))


str = "Sun Oct 14 13:47:03 CEST 2012"

x = re.search("13:47:03", str)
print (x)
x = re.search("([0-9][0-9]:[0-9][0-9]:[0-9][0-9])", str)
print (x.group(1))

x = re.search("([0-9]{2}:[0-9]{2}:[0-9]{2})", str)
print (x.group(1))

x = re.search("(\d\d:\d\d:\d\d)", str)
print (x.group(1))

x = re.search("(\d{2}:\d{2}:\d{2})", str)
print (x.group(1))

x = re.search("(.{2}:.{2}:.{2})", str)
print (x.group(1))


x = re.search("\b(?P<hours>\d\d):(?P<minutes>\d\d):(?P<seconds>\d\d)\b", str)
print (x.group())
print (x.group('hours'))
print (x.group('minutes'))
print (x.group('seconds'))
print (x.start('minutes'))
print (x.end('minutes'))


text="A fat cat doesn't eat oat but a rat eats bats."
allMatches = re.findall("[force]at", text)
print(allMatches)

str = "Course location is London or Paris!"
Matches = re.search("location.*(London|Paris|Zurich|Strasbourg)",str)
print(matches.group())

fh = open('regExInput.txt').readlines()

for line in fh:
	if re.search('(Python|systems)',line):
		print (line)

for line in fh:
	if re.search('(Python|systems)',line): print (line)

for line in fh:
	match = re.search('(Python|systems)',line)
	if match:
		print (match.group())

		
for line in fh:
	print(re.sub('(Python|systems)','#####',line))
 
  
for line in fh:
	match = re.search('(Python|systems)',line)
	if match:
		print (line.replace(match.group(),'####'),end='')

		
'''
Compiled regular objects usually are not saving much time, because Python internally compiles AND CACHES regexes whenever you use them with re.search() or re.match(). The only extra time a non-compiled regex takes is the time it needs to check the cache, which is a key lookup of a dictionary
'''

pattern = re.compile('(Python|systems)')
for line in fh:
	if re.search(pattern,line):
		print (line, end='')
		
pattern = re.compile('(Python|systems)', re.IGNORECASE)
#pattern = re.compile('(Python|systems)', re.I)
for line in fh:
	if re.search(pattern,line):
		print (line, end='')
		

pattern = re.compile('(Python|systems)')
for line in fh:
	if re.search(pattern,line):
		print (pattern.sub('######', line), end='')


