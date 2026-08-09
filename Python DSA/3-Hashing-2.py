numbers = [1, 2, 2, 3, 1, 4, 2, 3, 3]
Store = {}
for i in numbers:
    if i in Store:
        Store[i]+=1
    else:
        Store[i]=1
print(Store)