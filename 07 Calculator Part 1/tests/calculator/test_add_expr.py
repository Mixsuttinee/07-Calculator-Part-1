"""Test case for Multiplication """
#standard library
#3rd party library
import pytest
#Project library
from calculator.data_type import FactorialTerm,Number
from calculator.data_type import PowerTerm, UnaryTerm
from calculator.data_type import AddExpr

@pytest.mark.parametrize(
    "op, left, right, expected",
    [
        ("+",Number(1), Number(0), 1),
        ("-",Number(5), Number(0), 5),
        ("+",Number(0), Number(7), 7),
        ("-",Number(22), Number(6), 16),
        ("+",Number(2), FactorialTerm(Number(3)), 8),
        ("-",FactorialTerm(Number(3)), UnaryTerm("-", Number(5)), 11),
        ("+",PowerTerm(FactorialTerm(Number(3)), Number(2)), UnaryTerm("", Number(1)), 37),
    ]
)
def test_mul_expr(left, right, expected,op):
    #arrange
    expr = AddExpr(op, left, right)
    #act
    result = expr.execute()
    #assert
    assert result == expected