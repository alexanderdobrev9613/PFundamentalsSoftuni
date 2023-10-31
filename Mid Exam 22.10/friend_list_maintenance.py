friends_list = input().split(', ')
friends_list_og = friends_list.copy()
blacklisted_names = []
lost_names = []

while True:
    command = input().split()
    current_command = command[0]
    if current_command == 'Report':
        break

    elif current_command == 'Change':
        index_change, new_name = int(command[1]), command[2]
        if 0 <= index_change < len(friends_list):
            current_name = friends_list[index_change]
            friends_list[index_change] = new_name
            print(f'{current_name} changed his username to {new_name}.')

    elif current_command == 'Error':
        index = int(command[1])
        if 0 <= index < len(friends_list):
            if friends_list_og[index] not in blacklisted_names and \
                    friends_list_og[index] not in lost_names:
                lost_names.append(friends_list[index])
                print(f'{friends_list_og[index]} was lost due to an error.')
                friends_list[index] = 'Lost'

    elif current_command == 'Blacklist':
        name = command[1]
        if name in friends_list:
            blacklist_index = friends_list.index(name)
            friends_list[blacklist_index] = 'Blacklisted'
            print(f'{name} was blacklisted.')
            blacklisted_names.append(name)
        else:
            print(f'{name} was not found.')

print(f'Blacklisted names: {len(blacklisted_names)}')
print(f'Lost names: {len(lost_names)}')
print(' '.join(friends_list))
