def blacklist():
    if command[1] in friends_list:
        blacklisted_names.append(command[1])
        blacklist_index = friends_list.index(command[1])
        friends_list[blacklist_index] = 'Blacklisted'
        print(f'{command[1]} was blacklisted.')
    else:
        print(f'{command[1]} was not found.')

def error_func():
    if 0 <= int(command[1]) < len(friends_list):
        if friends_list_og[int(command[1])] not in blacklisted_names and \
                friends_list_og[int(command[1])] not in lost_names:
            lost_names.append(friends_list[int(command[1])])
            print(f'{friends_list_og[int(command[1])]} was lost due to an error.')
            friends_list[int(command[1])] = 'Lost'
def change_func():
    if 0 <= int(command[1]) < len(friends_list):
        friends_list[int(command[1])] = command[2]
        print(f'{friends_list_og[int(command[1])]} changed his username to {command[2]}.')


friends_list = input().split(', ')
friends_list_og = friends_list.copy()
blacklisted_names = []
lost_names = []

while True:
    command = input().split()
    if 'Report' in command:
        break
    if command[0] == 'Blacklist':
        blacklist()
    elif command[0] == 'Error':
        error_func()
    elif command[0] == 'Change':
        change_func()


print(f'Blacklisted names: {len(blacklisted_names)}')
print(f'Lost names: {len(lost_names)}')
print(' '.join(friends_list))
