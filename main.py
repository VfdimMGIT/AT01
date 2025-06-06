def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('На ноль делить нельзя')
    return a / b

def check(number):
    return number % 2 == 0

def modulo(a, b):
    """Вычисляет остаток от деления a на b с обработкой деления на ноль"""
    if b == 0:
        raise ValueError('На ноль делить нельзя')
    return a % b