#Directory layout of a project

## One-off Script
Mostly for Beginer. Not recommend for project except 

project
    +- calculater.py
    +- test_calculator.py

should not be used

## Installable Single Package
Application source code are in one directory (package)

Project/
│
├── calculator/
│   ├── __init__.py
    ├──binary_operator
    │   ├── __init__.py
    │   ├── add_operator.py
    │   ├── Multiply_operator.py
    │   ├── subtract_operator.py
    │   ├── divide_operator.py
    │   
    └── unary_operator
    │   ├── __init__.py
    │   ├── unary_minus_operator.py
    │   ├── factorial_operator.py
    │   ├── ................

│
├── tests/
│   └── calculator
        ├──__init__.py 
            ├──binary_operator
            │   ├── __init__.py
            │   ├── test_add_operator.py
            │   ├── test_Multiply_operator.py
            │   ├── test_subtract_operator.py
            │   ├── test_divide_operator.py
            │   
            └── unary_operator
            │   ├── __init__.py
            │   ├── test_unary_minus_operator.py
            │   ├── test_factorial_operator.py
            │   ├── ................

## Application with Internal Packages

Project/
│
├── src/
    ├── calculator/
        ├── __init__.py
        ├──binary_operator
        │   ├── __init__.py
        │   ├── add_operator.py
        │   ├── Multiply_operator.py
        │   ├── subtract_operator.py
        │   ├── divide_operator.py
        │   
        └── unary_operator
        │   ├── __init__.py
        │   ├── unary_minus_operator.py
        │   ├── factorial_operator.py
        │   ├── ................

│
├── tests/
    ├── __init__.py 
│   └── calculator
        ├──__init__.py 
            ├──binary_operator
            │   ├── __init__.py
            │   ├── test_add_operator.py
            │   ├── test_Multiply_operator.py
            │   ├── test_subtract_operator.py
            │   ├── test_divide_operator.py
            │   
            └── unary_operator
            │   ├── __init__.py
            │   ├── test_unary_minus_operator.py
            │   ├── test_factorial_operator.py
            │   ├── ................
