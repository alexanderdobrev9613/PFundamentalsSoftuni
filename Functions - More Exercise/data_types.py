command = input()
object = input()

def function():
    if command == 'int':
        result = int(object) * 2

    if command == 'real':
        result = f'{(float(object) * 1.5):.2f}'

    if command == 'string':
        result = f'${object}$'

    return result



print(function())