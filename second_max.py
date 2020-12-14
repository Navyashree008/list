num=[50,56,40,23,70,12,5,10,7]
max1=num
max2=0
max3=0
i=0
while i<len(num):
    if max1[i] >max2:
        max2=max1[i]
# print(max2)
    j=0
    while j<len(num):
        if max1[j] < max2:
            a = max1[j]
            if a > max3:
                max3 = a
        j+=1
    i+=1
print(max3)