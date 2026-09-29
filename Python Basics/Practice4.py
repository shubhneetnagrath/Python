def find_min(numbers):
   i = numbers[0]
   for n in numbers:
      if n<=i:
         i=n
   return(i)
        