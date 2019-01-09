#File management
# Modes
# read - r
# write - w 
# append - a

#Syntax : fileObject = open(<Input file>, <Mode>)

#File read
fh = open("filetest.txt", 'r')

for line in fh:
	print (line)

fh.close()
	
fh = open("filetest.txt")

for line in fh:
	print (line.strip())

fh.close()

#with method
with open("filetest.txt") as fh:
	for line in fh:
		print (line.strip())


#Write method
fh = open("fileHandlingOutput.txt", 'w')
fh.write("This is written from file write method\n")
fh.close()

#Both read and write in file
fhIn = open("filetest.txt")
fhOut = open("fileHandlingOutput.txt","w")
i = 1
for line in fhIn:
    print(line.strip())
    fhOut.write(S(i) + ": " + line)
    i = i + 1
fhIn.close()
fhOut.close()

#append method
fh = open("fileHandlingOutput.txt", 'a')
fh.write("This is written from file write method")
fh.close()

#Get the file into a list
fh = open("filetest.txt").readlines()
print (fh)
print "__________________"
print (fh[1])

#Get the file into a String
fh = open("filetest.txt").read()
print (fh)

#File read by specified number of bytes
fh = open("filetest.txt").read(10)
print (fh)


#Get the first line from file into a String
fh = open("filetest.txt").readline()
print (fh)


## Renaming a file
#Syntax : os.reneame(<old file name>, <new file name>)

import os

os.rename("oldFile.txt", "newfile.txt")

## remove a file
#Syntax : os.remove(<file>)

os.remove("newfile.txt")


Dir = "Test"
os.mkdir(Dir)

os.rmdir(Dir)

os.chdir(Dir)

print (os.getcwd())

