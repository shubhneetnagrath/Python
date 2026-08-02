text = "aaabbc"
new_text = ""
Y = ""
X = 1
for i in text:
    if Y==i:
        X+=1
    else:
        new_text=new_text+Y+str(X)
        Y=i
        X=1
print (new_text)
        