cards_list = input().split(', ')
count_of_commands = int(input())

for i in range(count_of_commands):
    command = input().split(', ')

    if command[0] == 'Add':
        if command[1] not in cards_list:
            cards_list.append(command[1])
            print('Card successfully added')
        else:
            print('Card is already in the deck')
    elif command[0] == 'Remove':
        if command[1] in cards_list:
            cards_list.remove(command[1])
            print('Card successfully removed')
        else:
            print('Card not found')
    elif command[0] == 'Remove At':
        if 0 <= int(command[1]) < len(cards_list):
            cards_list.pop(int(command[1]))
            print('Card successfully removed')
        else:
            print('Index out of range')
    elif command[0] == 'Insert':
        if 0 <= int(command[1]) < len(cards_list):
            if command[2] not in cards_list:
                cards_list.insert(int(command[1]), command[2])
                print('Card successfully added')
            else:
                print('Card is already added')
        else:
            print('Index out of range')

print(', '.join(cards_list))

