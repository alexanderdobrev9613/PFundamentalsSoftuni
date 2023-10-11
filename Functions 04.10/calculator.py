def add(a,b):
    return a + b

def calculator():
    operation = input('Enter the operation (+, -, *, /):')
    num1 = float(input('Enter the first number:'))
    num2 = float(input('Enter the secod number:'))
    result = 0

    if operation == '+':
        result = add(num1, num2)

    print(f'{result:.2f}')

calculator()