import pytest
from quadratic import solve_quadratic

def test_repeated_root():
    assert solve_quadratic(1,2,1) == -1

def test_distinct_root():
    assert solve_quadratic(1,4,3) == -3.0,-1.0

def test_complex_root():
    assert solve_quadratic(1,4,5) == ((-2-1j),(-2+1j))

def test_a_zero():
    assert solve_quadratic(0,1,2) == 'a must not equal 0 in a quadratic'

def test_negative():
    assert solve_quadratic(-1,-4,-3) == (-1.0,-3.0)

def test_string():
    assert solve_quadratic('A',-4,-3) == 'Please enter a number for a,b and c'

def test_large_val():
    assert solve_quadratic(10,-80,150) == (3,5)

def test_distinct_root():
    assert solve_quadratic(1.35,8.27,3.45) == (pytest.approx(-5.675660143450456), pytest.approx(-0.4502657824754694))
