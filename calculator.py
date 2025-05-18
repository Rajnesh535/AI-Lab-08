def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):

    negative = False
    if b < 0:
        b = -b
        negative = not negative
    if a < 0:
        a = -a
        negative = not negative

    result = 0
    for _ in range(int(b)):
        result = add(result, a)

    return -result if negative else result

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")

    negative = False
    if a < 0:
        a = -a
        negative = not negative
    if b < 0:
        b = -b
        negative = not negative

    quotient = 0
    sum_ = 0
    while sum_ + b <= a:
        sum_ = add(sum_, b)
        quotient = add(quotient, 1)

    return -quotient if negative else quotient

def calculator(a, b, operation):
    if operation == '+':
        return add(a, b)
    elif operation == '-':
        return subtract(a, b)
    elif operation == '*':
        return multiply(a, b)
    elif operation == '/':
        return divide(a, b)
    else:
        raise ValueError("Unsupported operation. Use +, -, *, or /.")

print(calculator(2, 4, '*'))
print(calculator(9, 6, '/'))
print(calculator(5, 8, '+'))
print(calculator(3, 10, '-'))
