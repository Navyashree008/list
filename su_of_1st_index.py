a = [[1,2,3],[4,5,6],[7,8,9]]
i = 0
sum1 = 0
while i < len(a):
    sum1 = 0
    j = 0 
    while j < len(a[i]):
        sum1 = sum1 + a[i][j]
        j+=1
    if i == 1 :
        print(sum1)
        break
    i+=1
