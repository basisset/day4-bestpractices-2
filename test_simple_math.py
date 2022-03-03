# test_simple_math.py
import simple_math as sm

def test_simple_add():
    assert sm.simple_add(1,2) == 3

def test_simple_sub():
    assert sm.simple_sub(1,2) == -1
    
def test_simple_mult():
    assert sm.simple_mult(1,2) == 2

def test_simple_div():
    assert sm.simple_div(1,2) == 0.5

def test_poly_first():
    assert sm.poly_first(3,2,1) == 5

def test_poly_second():
    assert sm.poly_second(4,3,2,1) == 27 #11 + 16 

