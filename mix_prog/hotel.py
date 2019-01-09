print ("**** welcome to the python hotel")

print("<<<<<<<MENU>>>>>>>>>>")
print ("1.chapati     			price:20")
print ("2.curry					price:30")
print ("3.daal					price:40")
print ("4.raita					price:10")
print ("5.egg masala			price:80")
print ("6.biryani				price:100")
print ("7.icecream				price:50")
print ("8.chiken masala			price:120")
print ("9.juice					price:40")
print ("10.gulab jamun			price:60")
sum=0

menu={"chapati":1,"curry":2,"daal":3,"raita":4,"egg masal":5,"biryani":6,"icecream":7,"chicken masala":8,"juice":9,"gulab jamun":10}
price={1:20,2:30,3:40,4:10,5:80,6:100,7:50,8:120,9:40,10:60}
n=int(input("Enter the number of item order::"))

for i in range(0,n):
	p=int(input("select the item:"))
	if p==menu['chapati']:
		 sum+=price[1]
		 print("total price %d" % sum)
	if p==menu['curry']:
		sum+=price[2]
		print("total price %d" % sum)
	if p==menu['daal']:
		sum+=price[3]
		print("total price %d" % sum)
	if p==menu['raita']:
		sum+=price[4]
		print("total price %d" % sum)
	if p==menu['egg masal']:
		sum+=price[5]
		print("total price %d" % sum)
	if p==menu['biryani']:
		sum+=price[6]
		print("total price %d" % sum)
	if p==menu['icecream']:
		sum+=price[7]
		print("total price %d" % sum)
	if p==menu['chicken masala']:
		sum+=price[8]
		print("total price %d" % sum)
	if p==menu['juice']:
		sum+=price[9]
		print("total price %d" % sum)
	if p==menu['gulab jamun']:
		sum+=price[10]
		print("total price %d" % sum)



