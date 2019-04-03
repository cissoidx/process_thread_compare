import numpy as np

def fib():
    """
    waste time using fib calculation
    """
    n = 1000000
    a = 1
    b = 1
    while n:
        n -=1
        a,b = b, a+b
    return b

def np_dot():
    """
    waste time using numpy dot
    """
    a = np.ones((100,100,100))
    b = np.ones((100,100,100))
    _ = np.dot(a,b)
    return _

def waste_time():
    return np_dot()
