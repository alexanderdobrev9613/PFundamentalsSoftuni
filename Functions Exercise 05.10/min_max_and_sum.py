sequence = input()
integer_list = list(map(int, sequence.split()))

min = min(integer_list)
max = max(integer_list)
sum = sum(integer_list)


print(f'The minimum number is {min}')
print(f'The maximum number is {max}')
print(f'The sum number is: {sum}')