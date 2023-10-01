gifts = input().split()
command = input().split()

while command[0] != 'No' and command[1] != 'Money':
    if command[0] == 'OutOfStock':
        gift = command[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = 'None'
    elif command[0] == 'Required':
        index = int(command[2])
        if 0 < index < len(gifts):
            gift = command[1]
            gifts[index] = gift
    elif command[0] == 'JustInCase':
        gifts[-1] = command[1]

    command = input().split(' ')

while 'None' in gifts:
    gifts.remove('None')


print(' '.join(gifts))