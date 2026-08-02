numbers = [0, 1, 0, 3, 12]
num =[]
Zero = 0
for i in numbers:
    if i == 0:
        Zero += 1
    else:
        num.append(i)

for _ in range(Zero):
    num.append(0)
print(num)
