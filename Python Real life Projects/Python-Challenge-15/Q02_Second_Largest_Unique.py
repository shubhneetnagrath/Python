numbers = [10, 9,10,]
numberscopy = numbers.copy() 
x = max(numberscopy)
numberscopy = [n for n in numberscopy if n != x]
if not (numberscopy) :
    print("No second largest unique number")
else:
    y = numberscopy[0]

    for i in numberscopy:
        if i > y:
            y = i

    print(y)

    numbers = [1, 2, 3, 4, 5]
x = numbers[-1]
numbers.pop(-1)
numbers1 = numbers.copy()
numbers.clear()
numbers.append(x)
numbers.extend(numbers1)
print(numbers)
