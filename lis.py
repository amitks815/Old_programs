list1=[1,2,3,4,5]
list2=[6,7,8,9]
list3=list1+list2

print("list after concatination:",end="")
for i in range(0,len(list3)):
	print (list3[i],end="")


lis = [2, 1, 3, 5,3, 4,7,7,8,9,3,4,5]
 
# using index() to print first occurrence of 3
# prints 5
print ("The first occurrence of 3 after 3rd position is : ", end="")
print (lis.index(3, 3, 10))
 
# using count() to count number of occurrence of 3
print ("The number of occurrences of 3 is : ", end="")
print (lis.count(3))


li=[1,2,3,4,5,6,7,8]

del li[2:5]

print(li)