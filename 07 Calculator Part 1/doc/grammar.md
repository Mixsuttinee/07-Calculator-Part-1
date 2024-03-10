# Grammar for the calculator

## Operator Precedence
| Precedence | Operator | Associativity |
|------------|----------|---------------|
|   0        |     (    |    R to L     |
|   1        |   " ! "  |    L to R     |
|   2        |     ^    |    R to L     |
|   3        | Unary-/+ |    R to L     |
|   4        | *,/,%    |    L to R     |
|   5        |    +,-   |    L to R     |


## Version 0 (Number)
The arithmetic expression is only a number

...
Arimathmetic Expression (AE) = Number

## Version 1 (Factorial)
Add the factorial operation.

...
Arimathmetic Expression (AE) = FactExpr
FactExpr =Number {" ! "}
...

## Version 2 (Power)
Add   the power expression.

...
Arimathmetic Expression (AE) = PowerExpr
PowerExpr = FactExpr {^ PowerExpr }
FactExpr = Number {" ! "}
...

## Version 3 : Unary
Add   the unary -/+ expression.

...
Arimathmetic Expression (AE) = UnaryExpr
UnaryExpr = [- | +] PowerExpr
PowerExpr = FactExpr {^ PowerExpr }
FactExpr = Number {" ! "}
...

## Version 4 : Multiplication
Add   the Multiplication expression.

...
Arimathmetic Expression (AE) = MulExpr
MulExpr = UnaryExpr { (" * " | "/" | "%") UnaryExpr }
UnaryExpr = [ "-" | "+" ] PowerExpr
PowerExpr = FactExpr {^ PowerExpr }
FactExpr = Number {" ! "}
...

## Version 5 : Addition
Add   the Multiplication expression.

...
Arimathmetic Expression (AE) = AddExpr
AddExpr = MulExpr   { (" + " | "-" ) MulExpr }
MulExpr = UnaryExpr { (" * " | "/" | "%") UnaryExpr }
UnaryExpr = [ "-" | "+" ] PowerExpr
PowerExpr = FactExpr {^ PowerExpr }
FactExpr = Number {" ! "}
...

## Version 6 : Parenthesis
Add   the Multiplication expression.

...
Arimathmetic Expression (AE) = AddExpr
AddExpr = MulExpr   { (" + " | "-" ) MulExpr }
MulExpr = UnaryExpr { (" * " | "/" | "%") UnaryExpr }
UnaryExpr = [ "-" | "+" ] PowerExpr
PowerExpr = FactExpr {^ PowerExpr }
FactExpr = Primary {" ! "}
Primary = Number | "(" AE ")"
...

## Lexical Grammar
operator = {"+", "-" , "*" , "/" , "%", "^", "!", "(" | ")"}
LParen = "("
RParen = ")"
Addop = "+" | "-"
Mulop = "*" | "/" | "%"
Powerop = "^"
Facop = "!"
Number = Digit {Digit} 
Digit = "0" | ... | "9"
