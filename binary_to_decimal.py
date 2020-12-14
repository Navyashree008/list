binary_number=[1,0,0,1,1,0,1,1]
total=0
a=len(binary_number)-1
i=0
while i<len(binary_number):
    # a=length-a
    total=total+binary_number[i]*(2**a)
    a=a-1
    i+=1
print(total)

