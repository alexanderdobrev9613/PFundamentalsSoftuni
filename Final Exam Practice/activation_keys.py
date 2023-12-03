raw_activation_key = input()

while True:
    command = input().split('>>>')

    if command[0] == 'Generate':
        print(f'Your activation key is: {raw_activation_key}')
        break
    elif command[0] == 'Contains':
        substring = command[1]
        if substring in raw_activation_key:
            print(f'{raw_activation_key} contains {substring}')
        else:
            print('Substring not found!')
    elif command[0] == 'Flip':
        upper_lower, start_index, end_index = command[1], int(command[2]), int(command[3])
        substring = raw_activation_key[start_index:end_index]     #moje bi bez -1
        if upper_lower == 'Upper':
            raw_activation_key = (raw_activation_key[:start_index] + substring.upper() + raw_activation_key[end_index:])
        elif upper_lower == 'Lower':
            raw_activation_key = (raw_activation_key[:start_index] + substring.lower() + raw_activation_key[end_index:])
        print(raw_activation_key)
    elif command[0] == 'Slice':
        first_index, last_index = int(command[1]), int(command[2])
        raw_activation_key = raw_activation_key[:first_index] + raw_activation_key[last_index:]
        print(raw_activation_key)