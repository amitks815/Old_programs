#get user inputs
name = input("What's your name? ")
print("Nice to meet you " + name + "!")
age = input("Your age? ")
print("So, you are are already " + str(age) + " years old, " + name + "!")


foods = input("What is your favourite foods?")
print (type(foods))
print ("I too love this foods" +  foods)

person = input("Your name please!")
print ('Hello',person,'!')
print ('Hello' + person +'!')

person = input("Your name please!")
print ('Hello ',person,'!', sep='')

raw_input("Press any key to exit!!!\n")

s = raw_input("Enter the value:") # new line will be automatically stripped 
print str

name = raw_input("What's your name? ")
print("Nice to meet you " + name + "!")
age = raw_input("Your age? ")
print("So, you are are already " + str(age) + " years old, " + name + "!")

age = raw_input("Your age? ")
print (type(age), age) # type is str

age = raw_input("Your age? ")
age = int(age)
print (type(age), age) # type is int


spots = raw_input("What is your favourite spots?")
print ("I too love this spots" +  spots)

print (type(spots)) #Type is str

spots = eval(raw_input("What is your favourite spots?"))
print (type(spots), spots ) #Type is list

spots = list(raw_input("What is your favourite spots?")) # casting function
print (type(spots), spots) #Expectation mismatch

amount = float(raw_input("Enter amount: ")) 
inrate = float(raw_input("Enter Interest rate: ")) 
period = int(raw_input("Enter period: ")) 
value = 0 
year = 1 
while year <= period:
    value = amount + (inrate * amount)
    print ("Year %d Rs. %.2f" %(year, value))
    amount = value
    year = year + 1 

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %s old, %r tall and %r heavy." % (
    age, height, weight) # %r for debugging purpose


#Diference between input and raw_input
bike = input("Enter the bike name: ") # len('Honda') get interprets 

print bike

bike = raw_input("Enter the bike name: ") # len('Honda') no interpretation(raw input and treats a string)

print bike


