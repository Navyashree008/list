# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# i = 0
# while i < len(marks):
#     sum1 = 0
#     j = 0
#     while j < len(marks[i]):
#         sum1 = sum1 + marks[i][j]
#         j+=1
#         avarage = sum1 // j
#     print("avarage of" ,i ,"list is",avarage)
#     i+=1


marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78],[87, 67, 49, 68, 88]]
i = 0
while i < len(marks):
    sum1 = 0
    j = 0
    while j < len(marks[i]):
        sum1 = sum1 + marks[i][j]
        j+=1
        avarage = sum1 // j
    print("avarage of" ,i ,"list is",avarage)
    i+=1
