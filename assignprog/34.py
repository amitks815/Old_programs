list1=[10,20,30,40,50]
list2=[1,2,3,4,5]
list3=[99,88,77,111,23]

print "list 1 =", list1
print "list 2=", list2
print "list 3=", list3
maxlist=[]
minlist=[]

count1=2
count2=2
count3=2

while(count1>0):
    max1=max(list1)
    min1=min(list1)
    maxlist.append(max1)
    minlist.append(min1)
    list1.remove(max1)
    list1.remove(min1)
    count1-=1

while(count2>0):
    max2=max(list2)
    min2=min(list2)
    maxlist.append(max2)
    minlist.append(min2)
    list2.remove(max2)
    list2.remove(min2)
    count2-=1

while(count3>0):
    max3=max(list3)
    min3=min(list3)
    maxlist.append(max3)
    minlist.append(min3)
    list3.remove(max3)
    list3.remove(min3)
    count3-=1

maxlist.sort()
minlist.sort()

print "Maximum elements from 3 lists in sorted order", maxlist
print "Minimum elements from 3 lists in sorted order", minlist

len1=len(maxlist)
len2=len(minlist)
avg1=0;avg2=0

for i in maxlist:
    avg1=avg1+i
for j in minlist:
    avg2=avg2+j

print "Average of maximum elements is=", avg1/len1
print "Average of minimum elements is=", avg2/len2



