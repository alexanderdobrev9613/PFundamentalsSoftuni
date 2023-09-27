lines = int(input())
brackets = 0
last_bracket = ''
is_balanced = True
balance_counter = 0

for current_line in range(lines):
    symbol = input()
    if symbol == last_bracket:
        is_balanced = False
    if symbol == '(':
        balance_counter += 1
        brackets += 1
        last_bracket = symbol
    elif symbol == ')':
        balance_counter -= 1
        brackets += 1
        last_bracket = symbol
        if balance_counter < 0:
            is_balanced = False
            break

if brackets % 2 == 0 and is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')