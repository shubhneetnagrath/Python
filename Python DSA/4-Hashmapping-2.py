numbers = []
target = 9
numbers = sorted(numbers)
for i in numbers:
    if i>target:
       numbers.remove(i)
l,u = 0,-1
for i in numbers:
    
