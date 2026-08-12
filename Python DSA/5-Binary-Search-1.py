numbers = [3, 7, 11, 15, 19, 24, 31, 42, 50]
target = 31
left = 0
right = len(numbers) - 1

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        print(middle) 
        break

    elif numbers[middle] < target:
        left = middle + 1

    else:
        right = middle - 1
