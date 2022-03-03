"""
A collection of simple math operations
"""

def simple_add(a,b):
    """The sum of two numbers.
    """
    return a+b

def simple_sub(a,b):
    """The subtraction of two numbers.
    """
    return a-b

def simple_mult(a,b):
    """The multiplication of two numbers.
    """
    return a*b

def simple_div(a,b):
    """The division of two numbers.
    """
    return a/b

def poly_first(x, a0, a1):
    """The first order polynomial.
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """The second order polynomial.
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
