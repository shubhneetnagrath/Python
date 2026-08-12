thislist = ["red","blue","green"]
print(len(thislist))
print(type(thislist))
#list Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
#Access item from list
print(thislist[1])
#Access items from the last
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

print(thislist[-4:-1])
#Always smaller to bigger no. when accessing multiple elements.

print(thislist[2:5])
#Note: The search will start at index 2 (included) and end at index 5 (not included).

#Change the second Item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change the second and third Item by replacing it with one value
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Extension of one list into another
'''Extend function can be used with any two iterable and is not
limited to only lists,instead one tuple and one list can also be used.'''

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Remove "banana"
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove item at specific index no.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#OR use this
thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist)

#Delete the list, khatam ho gayi list as a entity , i.e. eradicate ho gyi
thislist = ["apple", "banana", "cherry"]
del thislist

#The clear() method empties the list.The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])