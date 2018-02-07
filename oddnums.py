numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_list = [] 

for x in numbers:
    if x % 2 != 0:
        odd_list.append(x)

print(odd_list)