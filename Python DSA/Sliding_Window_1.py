"""
The main idea is very simple:

Instead of repeatedly examining the same elements, maintain a "window"
 over a portion of the array/string and move that window efficiently.
"""
#Example of Sliding Window

numbers = [2, 1, 5, 1, 3, 2]

#Find the maximum sum of any 3 consecutive elements.
# Approach>>>
#[2, 1, 5] → 8
#[1, 5, 1] → 7
#[5, 1, 3] → 9
#[1, 3, 2] → 6

#The important part is that these are overlapping windows.

Index = 0
Temparory = 0
maximum = 0
while Index + 2 < len(numbers):
      Temparory= numbers[Index] + numbers[Index+1] + numbers[Index+2]
      if Temparory>=maximum:
        maximum=Temparory
      Index+=1
print(maximum)

