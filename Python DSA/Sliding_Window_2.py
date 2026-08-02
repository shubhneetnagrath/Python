
def maximum_window_sum(numbers, K):
 i=0
 Index = 0
 Temp =0
 while i<(K):
   Temp = Temp+numbers[i]
   i+=1
 max= Temp
 while Index+K<len(numbers):
     Temp= Temp + numbers[Index+K] - numbers[Index]
     Index+=1
     if Temp>max:
         max = Temp
 return(max)
