text = "madam"
Collection_list = []
for i in text:
    Collection_list.append(i)
Collection_list.reverse()
Palindrome = "".join(Collection_list)
if Palindrome == text:
    print("Yes it is a Palindrome")
else :
    print("No it is not a Palindrome")

#OR

text = "madam"
S=0
E=-1
for n in text:
    

