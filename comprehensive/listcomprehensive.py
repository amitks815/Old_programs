list=[1,2,3,4,5]

print([x*x for x in list])

num=[1,2,4,6,5,7,8,9,3]
my_list1=[n*n for n in num if n%2==0]
print(my_list1)

my_list2=[(letter,no) for letter in 'abcd'  for no in range(4)]
print(my_list2)