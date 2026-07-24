text = ""
Y=1
if text=="":
    print("Empty String")
    Y=0
else:
 for i in text:
    if i == " ":
        Y+=1
    
print("Words:",Y)

