text1 = ""
text2 = ""
Y=0
Z=0
if (not text1) and (not text2):
    print("Both Strings Are Empty")
elif len(text2)!=len(text1):
    print("Not Anagram")
else:
  for i in text1:
    for x in text1:
        if i==x:
            Y+=1
    for y in text2:
        if i==y:
            Z+=1
    if Y==Z:
        Y=0
        Z=0
        Criteria=1
        continue
    else:
        Criteria=0
        break
  if Criteria==0:
    print("Not Anagram")
  else:
    print("Anagram")

