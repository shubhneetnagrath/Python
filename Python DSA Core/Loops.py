#Basic Loop Syntaxs

#FOR LOOP
numbers=[1,3,36,4,47]

for i in numbers:
   break

for i in range (len(numbers)):
   break

for i in (0,10,2):   # 0, 2, 4, 6, 8
   break

for i in range(5, 0, -1):   # 5, 4, 3, 2, 1
   break

#WHILE LOOP
count = 1
while count <= 5:
    print(count)
    count += 1

# LOOP CONTROL STATEMENTS

# break — exit the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)          # prints 0 1 2 3 4

# continue — skip the rest of current iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)          # prints 1 3 5 7 9

# pass — do nothing (placeholder)
for i in range(5):
    pass              # useful when you plan to write code later


#Enumerate Basic
tasks = ["Write code", "Run tests", "Deploy app"]

for index, task in enumerate(tasks):
    print(f"Task {index}: {task}")

#  Place #1: Alice
#  Place #2: Bob
#  Place #3: Charlie


#Enumerate Advanced 
runners = ["Alice", "Bob", "Charlie"]

for rank, runner in enumerate(runners, start=1):
    print(f"Place #{rank}: {runner}")

#  [(65, 'a'), (66, 'b'), (67, 'c')]


items = ["A", "B", "C"]

# Simulating a step size of 10
for i, item in enumerate(items):
    virtual_index = i * 10
    print(f"Step {virtual_index}: {item}")

#  Step 0: A
#  Step 10: B
#  Step 20: C

