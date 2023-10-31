journal = input().split(', ')

while True:
    commands = input().split(' - ')
    if 'Craft!' in commands:
        break
    command, item = commands[0], commands[1]
    if command == 'Collect':
        if item not in journal:
            journal.append(item)
    elif command == 'Drop':
        if item in journal:
            journal.remove(item)
    elif command == 'Combine Items':
        combined = item.split(':')
        if combined[0] in journal:
            position_item_one = journal.index(combined[0])
            journal.insert(position_item_one + 1, combined[1])
    elif command == 'Renew':
        if item in journal:
            journal.remove(item)
            journal.append(item)


print(', '.join(journal))