import numpy as np


'''
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
'''

def calc_pow(info):
    """
    calculate pow(x,y)
    x**y
    """
    for i in range(300000):
        if i%50000 == 0:
            print(info)
        _ = pow(1000,1000)
    return _


def waste_time(info):
    return calc_pow(info)
