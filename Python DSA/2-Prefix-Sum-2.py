from itertools import accumulate
# same as memory management in java
numbers = [4, 2, 7, 1, 5]

prefix = [0] + list(accumulate(numbers))

print(prefix)
