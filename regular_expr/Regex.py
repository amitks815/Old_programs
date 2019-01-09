import re

file=open("reg.txt",'r')
obj=file.read()

print(re.findall("[a*]",obj))

''''
str1 = "Mayer is a very common Name"
str2 = "He is called Mayer but he isn't German."

print(re.match("Mayer", str1))
print(re.match("Mayer", str2))
print(re.search("^Mayer", str1))
print(re.search("M[ae]yer", str1))#Mayer
print(re.search("M[ae]yer", str2))#Meyer 
print(re.search("M[ae][iy]er", str1))#Mayer, Meyer, Maier, Meier
print(re.search("M[ae][iy]er", str2))#Mayer, Meyer, Maier, Meier
print("********************")
var1 = He is called gentle man but he isn't German.
Mayer is a very common Name

print(re.search("^Mayer", var1))
print(re.search("^Mayer", var1, re.MULTILINE))
print(re.search("^Mayer", var1, re.M))
print(re.match("^Mayer", var1, re.M))'''