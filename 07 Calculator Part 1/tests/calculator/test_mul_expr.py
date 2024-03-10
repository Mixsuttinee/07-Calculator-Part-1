"""Test case for Multiplication """
#standard library
#3rd party library
import pytest
#Project library
from calculator.data_type import FactorialTerm,Number
from calculator.data_type import PowerTerm, UnaryTerm
from calculator.data_type import MulExpr

@pytest.mark.parametrize(
    "op, left, right, expected",
    [
        ("*",Number(1), Number(0), 0),
        ("*",Number(5), Number(0), 0),
        ("/",Number(0), Number(7), 0),
        ("%",Number(22), Number(6), 4),
        ("*",Number(2), FactorialTerm(Number(3)), 12),
        ("*",FactorialTerm(Number(3)), UnaryTerm("-", Number(5)), -30),
        ("*",PowerTerm(FactorialTerm(Number(3)), Number(2)), UnaryTerm("", Number(1)), 36),
    ]
)
def test_mul_expr(left, right, expected,op):
    #arrange
    expr = MulExpr(op, left, right)
    #act
    result = expr.execute()
    #assert
    assert result == expected