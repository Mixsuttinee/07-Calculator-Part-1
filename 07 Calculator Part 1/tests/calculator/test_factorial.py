"""Factorial operations"""

#standard library
#3rd party library
import pytest
#Project library
from calculator.factorial import factorial
from calculator.data_type import FactorialTerm,Number


@pytest.mark.parametrize(
    "num, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120)
    ]
)
def test_factorial(num, expected):
    """Calculates the factorial """
    #arrange
    #act
    result = factorial(num)
    #assert 
    assert result == expected

@pytest.mark.parametrize(
    "fact_term, expected",
    [
        (Number(5), 5),
        (FactorialTerm(Number(5)), 120),
        (FactorialTerm(Number(4)), 24),
        (FactorialTerm(Number(3)), 6),
        (FactorialTerm(Number(2)), 2),
        (FactorialTerm(Number(1)), 1),
        (FactorialTerm(Number(6)), 720),
        (FactorialTerm(Number(0)), 1),
        (FactorialTerm(FactorialTerm(Number(3))), 720),
    ]    
)
def test_factorial_term(fact_term, expected):
    #arrange
    #act
    result = fact_term.execute()
    #assert
    assert result == expected