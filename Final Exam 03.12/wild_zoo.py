animals = {}
command = input().split(': ')
while True:
    if command[0] == 'EndDay':
        break
    elif command[0] == 'Add':
        tokens = command[1].split('-')
        name, needed_food_quantity, area = tokens[0], int(tokens[1]), tokens[2]
        if name not in animals.keys():
            animals[name] = {'needed_food': needed_food_quantity, 'area': area}
        else:
            animals[name]['needed_food'] += needed_food_quantity
    elif command[0] == 'Feed':
        tokens = command[1].split('-')
        name, food = tokens[0], int(tokens[1])
        if name in animals.keys():
            animals[name]['needed_food'] -= food
        if name in animals.keys() and animals[name]['needed_food'] <= 0:
            animals.pop(name)
            print(f"{name} was successfully fed")
    command = input().split(': ')

animals_per_area = {}
for animal, data in animals.items():
    area = data['area']
    if area in animals_per_area:
        animals_per_area[area] += 1
    else:
        animals_per_area[area] = 1

print('Animals:')
for name, animal_info in animals.items():
    print(f" {name} -> {animal_info['needed_food']}g")
print('Areas with hungry animals:')
for area, count in animals_per_area.items():
    print(f" {area}: {count}")

