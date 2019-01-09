def palindrome(str):
    if(str==str[::-1]):
        print str,"is a palindrome"
    else:
        print str,"is not a palindrome"
    return  

print "*****Print the output below using keyword arguments*****\n"

palindrome(str="malayalam")


def palindrome(str='liril'):
    if(str==str[::-1]):
       print str,"is a palindrome"
    else:
       print str,"is not a palindrome"
       return  

print "\n*****print the output below using default arguments*****\n"

palindrome()

