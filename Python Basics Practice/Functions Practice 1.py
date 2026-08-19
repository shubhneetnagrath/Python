#1. Write a function is_even(n) that returns True if n is even and False otherwise.
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
#2. Write a function largest(a, b, c) that returns the largest of three numbers without using max()
def largest(a, b, c):
    Store = []
    Store = [a, b, c]
    Store.sort()
    return Store[-1]
#3. Write a function count_vowels(text) that returns how many vowels (a, e, i, o, u) are in a string
def count_vowels(text):
    count = 0
    for i in text:
        if i in "aeiouAEIOU":
            count+=1
    return count
#4. Write a function reverse_string(text) that returns the reversed string.
def reverse_string(text):
    reversed_text = text[::-1]
    return reversed_text
#5. Write a function calculate_average(numbers) that returns the average of a list of numbers.
def calculate_average(numbers):
    Average =sum(numbers)/len(numbers)
    return Average