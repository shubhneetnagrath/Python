numbers = [1,2,3]
Common = []
for i in range(len(numbers)):
    y = numbers[i]
    for x in numbers:
        if y == x:
           Common.append(x)


result = Common.copy()

for items in numbers:
    result.remove(items)

unique = [item for item in numbers if item not in result]

if not unique:
    print("no non reapeting element ")
else:
    print(unique[0])


