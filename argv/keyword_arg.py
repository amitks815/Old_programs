from sys import argv
num=input('Enter the number:').split(' ')
print("nums are:",num)

list=[1,2,3,4,5]


def fun(*argv):
	print('list',list)

fun(*list)



def fun1(**kwarg):
	print('disct:',kwarg)
Dict = {'a':'append', 'b':'block','x':'extract','y':'yes'}
fun1(**Dict)