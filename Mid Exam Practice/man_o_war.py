pirate_ship = [int(s) for s in input().split('>')]
war_ship = [int(w) for w in input().split('>')]
max_capacity = int(input())

is_stalemate = True

while True:
    command = input().split()

    if command[0] == 'Retire':
        break
    
    if command[0] == 'Fire':
        if 0 <= int(command[1]) < len(war_ship):
            war_ship[int(command[1])] -= int(command[2])
            if war_ship[int(command[1])] <= 0:
                print(f'You won! The enemy ship has sunken.')
                is_stalemate = False
                break

    if command[0] == 'Defend':
        if 0 <= int(command[1]) < len(pirate_ship) and 0 <= int(command[2]) < len(pirate_ship):
            for sections in range(int(command[1]), int(command[2]) + 1):
                pirate_ship[sections] -= int(command[3])
                if pirate_ship[sections] <= 0:
                    print(f'You lost! The pirate ship has sunken.')
                    is_stalemate = False
                    break

    if command[0] == 'Repair':
        if 0 <= int(command[1]) < len(pirate_ship):
            pirate_ship[int(command[1])] += int(command[2])
            if pirate_ship[int(command[1])] > max_capacity:
                pirate_ship[int(command[1])] = max_capacity
                repair_value = max_capacity - int(command[2])

    if command[0] == 'Status':
        count = 0
        for status_section in pirate_ship:
            if status_section < max_capacity / 5:
                count += 1
        print(f'{count} sections need repair.')

if is_stalemate:
    pirate_status = sum(pirate_ship)
    war_status = sum(war_ship)
    print(f'Pirate ship status: {pirate_status}')
    print(f'Warship status: {war_status}')
