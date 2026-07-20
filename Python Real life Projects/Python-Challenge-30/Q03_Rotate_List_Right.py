numbers = [1, 2, 3, 4, 5]
x = numbers[-1]
numbers.pop(-1)
numbers1 = numbers.copy()
numbers.clear()
numbers.append(x)
numbers.extend(numbers1)
print(numbers)

#OR

numbers = [1, 2, 3, 4, 5]
x = numbers[4]
del numbers[4]
numbers.insert(0,x)
print(numbers)