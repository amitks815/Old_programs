
#string methods---count
str = "this is string example....wow!!!";
#sub = "i";
print ("str.count(sub, 4, 40) : ", str.count('i', 4, 40))
sub = "wow";
print ("str.count(sub) : ", str.count(sub))

#title
str = "This is string example....wow!!!";
print (str.title())

#join
s = "-";
seq = ("123","345","543"); # This is sequence of strings.
print (s.join( seq ))

#split
str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print (str.split( ))

def sum_of_list():
    list_item=[]
    x=int(input("Enter the no of elements require in list :"))
    for i in range(x):
        y=int(input("List elements :"))
        list_item.append(y)
        print("List = ", list_item)
    sum_no=0
    for z in list_item:
     sum_no += z
    return sum_no
print("The sum of the list is ",sum_of_list())