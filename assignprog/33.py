list=[10,20,30,40,50,60,70]

print "Original list=",list

list.append(80)

print "List output after value 80 is appended=", list

list[4]=100

print"List output after element 100 is inserted in 4th position=", list


list.sort()
print "sorted list is =", list
list.reverse()
print "Sorted list in reverse order=",list

del list[4:]


print "List output after removing last 3 elements", list
