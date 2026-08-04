numbers = [3, 5, 3, 2, 5, 3, 7, 2]

frequency = {}

for x in numbers:

    if x in frequency:
        frequency[x] += 1
    else:
        frequency[x] = 1

print(frequency)