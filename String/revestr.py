def reverse(s):
l=len(s)
p=[]
c=''
for i in range(0,l):
p.append(s[i])
p.reverse()
for i in p:
c+=i
return c
print(reverse('abcde'))