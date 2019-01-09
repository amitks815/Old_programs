print "program to check if a string is palindrome or not"
str=raw_input("Enter a string:=")

if(str==str[::-1]):
	print str,"is a palindrome string"
else:
	print str,"is not a palindrome string"

