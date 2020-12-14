# #pat 1
# def calculator(num1,num2,operation):
#     if operation  == "add":
#         return num1 +num2
#     elif operation == "subtract":
#         return num1 -num2
#     elif operation == "multiplication":
#         return num1 * num2
#     elif operation == "division"
#         return num1/num2
# print(calculator(6,3,"division"))

#part2
# def calculator(num1,num2,operation):
#     if operation  == "add":
#         return num1 +num2
#     elif operation == "subtract":
#         return num1 -num2
#     elif operation == "multiplication":
#         return num1 * num2
#     elif operation == "division":
#         return num1/num2
# num1 = 6
# num2 = 3
# add_result = num1+num2
# print(add_result)
# sub_result = num1-num2
# print(sub_result)
# multiple_result = num1*num2
# print(multiple_result)
# divid_result = num1/num2
# print(divid_result)



def calculator(num1,num2,operation):
    if operation  == "add":
        return num1 +num2
    elif operation == "subtract":
        return num1 -num2
    elif operation == "multiplication":
        return num1 * num2
    elif operation == "division":
        return num1/num2
list1 = []
num1 = [1,2,3,4,5]
num2 = [3,4,5,6,7]
for i in range(len(num1)):
    #for j in range(len(num2)):
    calculator(num1[i],num2[i],"multiplication")
    mult_result = num1[i]*num2[i]
    list1.append(mult_result)
print(list1)