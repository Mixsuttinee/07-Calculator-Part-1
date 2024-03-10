"""Token"""
#standard library
from enum import Enum
from collections import namedtuple
#3rd party library
#Project library

TokenType = Enum(
    "TokenType",
    [
        "ERROR",
        "UNKNOWN",
        "EMPTY",
        "NUMBER",
        "FAC_OP",
        "POWER_OP",
        "MUL_OP",
        'ADD_OP',
        "LEFT_OP",
        "RIGHT_OP",
    ]
)

Token = namedtuple(
    "Token",
    [
        "token_type",
        "lexeme"
    ]
)