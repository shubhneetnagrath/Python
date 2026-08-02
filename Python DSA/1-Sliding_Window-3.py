numbers =[2, 1, 5, 2, 3, 2]
target =7
if 7 in numbers:
    print(1)
else:
    X=0
    Length=float("inf")
    S=0
    sum = 0
    for i in range(len(numbers)):
           sum=sum+ numbers[S]
           S+=1
           while sum>=7:
            if Length>=S-X:
               Length= S-X
               sum = sum - numbers[X]
               X+=1
          

print(Length if Length != float('inf') else 0)
           