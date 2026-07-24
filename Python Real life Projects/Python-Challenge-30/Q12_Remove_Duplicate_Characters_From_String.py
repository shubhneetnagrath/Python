text = "programming"
TextList =[]
for i in text:
    if i not in TextList:
            TextList.append(i)
result = ''.join(TextList)
print(result)