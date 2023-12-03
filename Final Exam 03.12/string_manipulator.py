string = input()

while True:
    command = input().split()
    if command[0] == 'End':
        break
    elif command[0] == 'Translate':
        char, replacement = command[1], command[2]
        for _ in string:
            if _ == char:
                string = string.replace(char, replacement)
                break
        print(string)
    elif command[0] == 'Includes':
        if command[1] in string:
            print('True')
        else:
            print('False')
    elif command[0] == 'Start':
        if string.startswith(command[1]):
            print('True')
        else:
            print('False')
    elif command[0] == 'Lowercase':
        string = string.lower()
        print(string)
    elif command[0] == 'FindIndex':
        indices = []
        token = command[1]
        for command[1], letter in enumerate(string):
            if token == letter:
                indices.append(command[1])
        if len(indices) > 0:
            print(max(indices))
    elif command[0] == 'Remove':
        start_index, count = int(command[1]), int(command[2])
        string = string[:start_index] + string[(start_index + count):]
        print(string)
