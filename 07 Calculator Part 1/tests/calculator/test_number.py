#standard library
#3rd party library
#Project library
from calculator.data_type import Number


def test_number():
    #arrange
    value = 5
    calc = Number(value)

    #act
    result =  calc.execute()

    #assert
    assert result == value