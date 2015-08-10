def myfunction(x,y):
    ''' (number, number) -> number
    Returns the value of x to the power of y
    >>> myfunction(2,3)
    8
    '''
    return x**y

def yet_another_fun(x,y,z):
    return x+y+z

def sumall(x,y,z):
    print("The sum is",x+y+z)
    return x+y+z, x-y-z

# [sth,another] = sumall(1,2,3)        # to obtain two return results

def halfpower(value1, value2):
    '''
    (number, number) -> float
    Returns half the value of value1 to the power of value2
    >>> halfpower(2,3)
    4.0
    >>> helfpower(2,5)
    16.0
    '''
    result = myfunction(value1, value2)/2
    return result






    
    
