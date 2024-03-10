"""Calculate factorial"""


def factorial(num):
    """Calculate factorial"""
    result = 1
    for value in range(1,num+1):
        result = result * value
    
    return result
