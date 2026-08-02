words = ["flower", "flow", "flight"]
S = 0
Y = ""
for i in words:
    for x in words:
      if S < len(i):
        if i[S]!=x[S]:
            break
        else:
            Y = Y + i[S]
            S+=1
print(Y)



