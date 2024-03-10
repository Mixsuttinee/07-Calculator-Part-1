"""Test case for power """
#standard library
#3rd party library
import pytest
#Project library
from calculator.data_type import FactorialTerm,Number
from calculator.data_type import PowerTerm

@pytest.mark.parametrize(
    "left, right, expected",
    [
        (Number(1), Number(0), 1),
        (Number(5), Number(0), 1),
        (Number(0), Number(7), 0),
        (Number(2), Number(6), 64),
        (Number(2), FactorialTerm(Number(3)), 64),
        (FactorialTerm(Number(3)), Number(2), 36),
    ]
)
def test_power_expr(left, right, expected):
    #arrange
    expr = PowerTerm(left, right)
    #act
    result = expr.execute()
    #assert
    assert result == expected