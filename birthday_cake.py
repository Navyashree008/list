list1=[]
i=0
num=int(input("enter no:"))
while i<num:
    num1=int(input("enter no"))
    list1.append(num1)
    i+=1
print(list1)
max1=list1
max2=0
j=0
while i<len(max1):
    if max1[j] > max2:
        max2=max1[j]
    j+=1
print(max2)
a=0
total=0
while a<len(list1):
    if list1[a]==max2:
        total+=1
    a+=1
print(total)