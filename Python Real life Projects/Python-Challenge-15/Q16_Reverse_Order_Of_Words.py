text = "I love Python" + " "
Y = ""
New_list=[]
for i in text:
    if i==" ":
        New_list.append(Y)
        Y=""
    else:
        Y = Y + i
S = 0
New_List2=[]
for x in New_list:
    S-=1
    New_List2.append(New_list[S])
result_space = " ".join(New_List2)
print(result_space)
    