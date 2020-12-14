# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# duplicate = []
# i = 0
# count = 0
# while i < len(n):
#     j = 0
#     while j < len(n):
#         count = 0
#         if n[i] == n[j]:
#             count = count+1
#             if count > 1:
#                 a.append(n[i])
#             #count = 0
#         j+=1
#         #count = 0
#     i+=1
# print(duplicate)

n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
duplicate = []
count = 0
for i in range(len(n)):
    for j in range(len(n)):
        if n[i] == n[j]:
            count = count+1
        if count > 1:
            if n[i] not in duplicate:
                duplicate.append(n[i])
    count = 0
print(duplicate)
print(count)