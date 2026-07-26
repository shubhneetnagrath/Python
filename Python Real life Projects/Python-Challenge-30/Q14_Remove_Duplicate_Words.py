text = "I love Python programming"
Y = 0
H = 0
Str =""
Long_Str=""
if not text:
  print("empty")
else:
  for i in text:
   if i == " ":
        Y=0
        Str=""
   else:
    Str = Str + i
    Y+=1
    if Y>=H and len(Str)>=len(Long_Str):
        H=Y
        Long_Str= Str
  print(H)
  print(Long_Str)