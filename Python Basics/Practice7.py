def has_pair(numbers, target):
    left = 0
    right = len(numbers)-1

    while right>left:
        if target == numbers[left] +numbers[right]:
            return(True)
        if target < numbers[right]+numbers[left]:
            right-=1
        if target > numbers[right]+numbers[left]:
            left+=1
    if target!= numbers[left]+numbers[right]:
        return(False)