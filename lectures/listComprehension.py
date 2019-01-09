##List comprehension
'''Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print Fahrenheit'''
num =[3,4,2,4,5,6,7,8,9]

my_list=[n*n for n in num]
print(my_list)
my_list1=[n*n for n in num if n%2==0]
print(my_list1)

my_list2=[(letter,no) for letter in 'abcd'  for no in range(4)]
print(my_list2)


f_name=['amit','atul','deepak','ram']
l_name=['kumar','singh','sharma','bhagat']

# dictinonary comprehansive

mydict={f_name:l_name for f_name,l_name in zip(f_name,l_name) }
print(mydict)

#set comprehensive
num=[1,2,1,2,3,4,3,5,6,5,7,8,9,7,4]

my_set={n for n in num}
print(my_setDict = {'a':'append', 'b':'block','x':'extract','y':'yes'})