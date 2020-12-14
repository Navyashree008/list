name1=[]
name =["n","i","t","i",'n']
length = len(name)
a = length-1
i = 0
while i < length:
    name1.append(name[a-i])
    i+=1
print(name1)
if name1==name:
    print("yes, its a palindrome")
else:
    print("no,its not a palindrome")