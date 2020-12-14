elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even = 0
odd = 0
i = 0
while i < len(elements):
    if i % 2 == 0:
        even = even + elements[i]
    else:
        odd = odd + elements[i]
    i+=1
print(even)
print(odd)