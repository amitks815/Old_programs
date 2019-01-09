def fib(num):
    n1=0
    n2=1
    print n1
    print n2
    for i in range(num-2):
        temp=n1+n2
        n1=n2
        n2=temp
        print temp
    return 


num=input("Enter the max elements for fibonacci series=")

fib(num)

