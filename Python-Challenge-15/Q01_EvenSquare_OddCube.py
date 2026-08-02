numbers = [2, 5, 8, 3, 10]
new_numbers =[]

for i in numbers:
    if (i%2) != 0:
        new_numbers.append(i**3)
    elif(i%2) == 0:
        new_numbers.append(i**2)
print(new_numbers)
