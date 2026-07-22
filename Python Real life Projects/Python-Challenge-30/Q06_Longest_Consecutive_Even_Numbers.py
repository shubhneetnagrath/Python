numbers = [2, 4, 6, 1, 8, 10]
y = 0
x = 0
for i in numbers:
    if i%2==0:
        x+=1
        if x>y:
            y = x
    elif i%2!=0:
        x = 0
print(y)