# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# length = len(marks)
# sum1 = 0
# sum2 = 0
# sum3 = 0
# i = 0
# while i<= 0:
#     a = 0
#     while a < len(marks[0]):
#         sum1 = sum1 + marks[0][a]
#         a+=1
#     #print(sum1)
#     b = 0
#     while b < len(marks[1]):
#         sum2 = sum2 + marks[1][b]
#         b+=1
#     #print(sum2)
#     c = 0
#     while c < len(marks[2]):
#         sum3 = sum3 + marks[2][c]
#         c+=1
#     #print(sum3)
#     i+=1
#     #length = length-length
# print(sum1 + sum2 + sum3)







marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78],[87, 67, 49, 68, 88]]
sum1 = 0
i = 0
while i<len(marks):
    j = 0
    while j < len(marks[i]):
        sum1 = sum1 + marks[i][j]
        j+=1
    i+=1
print(sum1)