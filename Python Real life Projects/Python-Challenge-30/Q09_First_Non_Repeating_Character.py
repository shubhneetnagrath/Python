text = "swiss"
if not text:
    print("No elements")
else:
 H = 1
 Y = 1
 Lowest= text[0]
 for i in text:
   Y = 0
   for x in text:
     if i == x:
       Y+=1
   if Y<=H :
     Lowest = i
     H=Y
     if H== 1:
       break
   Y = 0
 
 print(H)
 print(Lowest)
    

