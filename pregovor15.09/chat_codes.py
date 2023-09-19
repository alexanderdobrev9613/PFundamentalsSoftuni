n = int(input())

for i in range(n):
    current_n = int(input())
    if current_n == 88:
        print('Hello')
    elif current_n == 86:
        print('How are you?')
    elif current_n < 88:
        print('GREAT!')
    else:
        print('Bye.')