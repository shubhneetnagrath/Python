def myfunc(n):
    '''
    >def is used to define a function.

    >myfunc is the name of the function.

    >n is the parameter (input) that the function accepts.
    '''
    return abs(n-50)

'''
>abs() is a built-in Python function that
returns the absolute (positive) value of a number.

>n - 50 calculates the difference between n and 50.

>abs(n - 50) gives the distance of n from 50,The function returns this distance.

'''

thislist = [100,50,65,82,23]
thislist.sort(key=myfunc)
'''
>sort() sorts the list in place (it changes the original list).
>The key parameter tells Python how to compare the elements.
>Instead of comparing the numbers directly,
 Python calls myfunc() for each element and sorts based on the returned values.
'''
print(thislist)
