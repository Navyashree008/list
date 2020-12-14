# list1 = [[1,1,1],
#          [1,1,1],
#          [1,1,1]]
# #for sum of row
# i = 0
# sum1 = 0
# while i < len(list1):
#     j = 0
#     while j < len(list1[i]):
#         sum1 = sum1 + list1[i][j]
#         j+=1
#     i+=1
# print(sum1)
# #for sum of column
# i = 0
# col = 0
# while i < len(list1):
#     j = 0
#     while j < len(list1[i]):
#         col = col + list1[i][j]
#         j+=2
#     i+=1
# print(col)
students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
print (len(students))
print(len(marks))
length = len(students) # kyunki dono ki same length hai toh jiski bhi length le sakte ho
i = 0
while i < length:
	print(students[counter] + str(marks[counter]))
    i+=1
    