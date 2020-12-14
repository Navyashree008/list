number=[50,40,23,70,56,12,5,10,7]
max1=number
max2=0
i=0
while i<len(number):
    if max1[i] > max2:
        max2 = max1[i]
    i+=1
print(max2)