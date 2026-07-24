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
if not text:
    print("Empty String")
else:
 S=0
 E=-1
 for n in range(len(text)//2):
    if text[S]==text[E]:
        Pal=True
    else:
        Pal=False
        break
    S+=1
    E-=1
 if Pal==True:
    print("Yes it is a Palindrome")
 else:
    print("No it is not a Palindrome")
