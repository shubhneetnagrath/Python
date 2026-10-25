def Xyz (numbers,L,U):
    numberscopy =[]
    for i in range(len(numbers)):
       if i >=L and i<=U:
        numberscopy.append(numbers[i])
    return sum(numberscopy)

    

    
