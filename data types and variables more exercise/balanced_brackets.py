lines = int(input())
open_brackets = 0
closed_brackets = 0

for current_line in range(lines):
    symbol = input()
    if symbol == '(':
        open_brackets += 1
    if symbol == ')':
        closed_brackets += 1

if (open_brackets + closed_brackets) % 2 != 0:
    print('UNBALANCED')
else:
    print('BALANCED')