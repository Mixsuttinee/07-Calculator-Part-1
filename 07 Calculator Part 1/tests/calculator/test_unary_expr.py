"""Test case for Unary """
#standard library
#3rd party library
import pytest
#Project library
from calculator.data_type import FactorialTerm,Number
from calculator.data_type import PowerTerm
from calculator.data_type import UnaryTerm

@pytest.mark.parametrize(
    "operator ,operand, expected",
    [
        ("-", Number(3), -3),
        ("+", Number(7), 7),
        ("-", FactorialTerm(Number(3)), -6),
        ("+", FactorialTerm(Number(4)), 24),
        ("-", PowerTerm(Number(3),Number(2)), -9),
    ]
)
def test_unary_expr(operator, operand, expected):
    #arrange
    expr =  UnaryTerm(operator, operand)
    #act
    result = expr.execute()
    #assert
    assert result == expected