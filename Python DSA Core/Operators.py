#ARITHMETIC OPERATORS>>
#Basic > +,-,*,/
x = 10//3 # Floor Division (Answer as a integer only)
x = 10%3 # Remainder
x = 10**3 # Exponential

#ASSIGNMENT OPERATORS>>
x+=5            # Increament
x-=5            # Decreament
x *= 2          # x = x * 2  → 24
x /= 4          # x = x / 4  → 6.0
x //= 2         # x = x // 2 → 3.0
x %= 2          # x = x % 2  → 1.0
x **= 3         # x = x ** 3 → 1.0

#LOGICAL OPERATORS
x, y = True, False

print(x and y)   # False (both must be True)
print(x or y)    # True  (at least one True)
print(not x)     # False

#MEMBERSHIP OPERATOR
nums = [1, 2, 3, 4]
print(2 in nums)       # True
print(5 not in nums)   # True

#IDENTITY OPERATORS
a = [1, 2]
b = a
c = [1, 2]

print(a is b)      # True  (same object)
print(a is c)      # False (different objects)
print(a is not c)  # True
print(a == c)      # True  (same values)

#BITWISE OPERATORS (ON INTEGERS)

x & y   #And
x | y   #OR
x ^ y   #XOR
~x      #NOT (invert)

#OPERATOR PRECEDENCE 
#**
#~, +x, -x (unary)
#*, /, //, %
#+, -
#<<, >>
#&
#^
#|
#Comparisons (==, !=, <, etc.), is, in
#not
#and
#or
#Assignment (=, +=, etc.)

#Use parentheses when in doubt.