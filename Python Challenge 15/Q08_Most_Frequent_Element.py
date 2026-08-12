numbers = []
if not numbers:
    print("No elements")
else:
 H = 1
 Y = 1
 Highest_Freqeuncy_Element= numbers[0]
 for i in numbers:
   Y = 0
   for x in numbers:
     if i == x:
       Y+=1
   if Y>H :
     Highest_Freqeuncy_Element = i
     H=Y
   Y = 0
 
 print(H)
 print(Highest_Freqeuncy_Element)
    

