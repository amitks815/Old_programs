#Parameter unpacking
from sys import argv

print "My script is ", argv[0]
print "My name is ", argv[1]
print "My age is ", argv[2] #type is str
print "I am from ", argv[3]

script, name, age, location = argv 

print "My script is ", script
print "My name is ", name
print "My age is ", age #type is str
print "I am from ", location

print "Here is all parameters ", argv

print "Length of parameters ", len(argv)


script, userName = argv
prompt = '>> '

print "Hi %s, I'm the %s script." % (userName, script)
print "I'd like to ask you a few questions. "
print "Do you like %s." % userName
likes = raw_input(prompt)
print "where do you live %s?" % userName
lives = raw_input(prompt)
print "What is your hobby %s?" % userName
hobby = raw_input(prompt)

print """
Good, so you said %r about liking me.
You live in %r.
And your hobby is %r. Super!!!
""" % (likes, lives, hobby)











