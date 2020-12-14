elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even_sum = 0
odd_sum = 0
even = 0
odd = 0                                                                                                                                                                               
i = 0
while i < len(elements):
    if i % 2 == 0:
        even_sum = even_sum + elements[i]
        even =  even+1
    else:
        odd_sum = odd_sum + elements[i]
        odd = odd+1
    i+=1
even_avarage = even_sum // even
odd_avarage = odd_sum // odd
print(even_avarage)
print(odd_avarage)
print(even)
print(odd)
print(even_sum)
print(odd_sum)