numbers =[2, 1, 5, 2, 3, 2]
if 7 in numbers:
    print(1)
else:
    X=0
    S=0
    sum = 0
    for i in range(len(numbers)):
       if sum <7:
           sum=sum+ numbers[S]
           S+=1
       elif sum>7:
           sum = sum - numbers[X]
           X+=1
       elif sum==7:
           print(S-X)
           break