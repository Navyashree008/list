# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# i = 0
# a = 0
# n = 0
# t = 0
# x = 0
# u = 0
# while i < len(char_list):
#     if char_list[i] == "a":
#         a = a+1
#     elif char_list[i] == "n":
#         n = n+1
#     elif char_list[i] == "t":
#         t = t+1
#     elif char_list[i] == "x":
#         x = x+1
#     else:
#         u = u+1
#     i+=1
# print(a,'times a is repeated')
# print(n,"times n is reapeated")
# print(t,"times t i reapeated")



char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i = 0
c = []
while i < len(char_list):
    j = 0
    a =[]
    count = 0
    while j < len(char_list):
        if char_list[i] == char_list[j]:
            count = count+1
        j=j+1
    a.append(char_list[i])
    a.append(count)
    if a not in c:
        c.append(a)
    i=i+1
print(c)


