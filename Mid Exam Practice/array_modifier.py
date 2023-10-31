initial_values = input().split()
command = ''

while True:
    command = input().split()
    if command[0] == 'end':
        break
    if command[0] == 'swap':
        for numbers in initial_values:
            initial_values[int(command[1])], initial_values[int(command[2])] = initial_values[int(command[2])], initial_values[int(command[1])]
            break
    elif command[0] == 'multiply':
        for m_numbers in initial_values:
            multiplied = int(initial_values[int(command[1])]) * int(initial_values[int(command[2])])
            initial_values[int(command[1])] = str(multiplied)
            break
    elif command[0] == 'decrease':
        counter = 0
        for n in initial_values:
            initial_values.remove(n)
            n = int(n) - 1
            initial_values.insert(counter, n)
            counter += 1

result = str(initial_values)
print(', '.join(result))

