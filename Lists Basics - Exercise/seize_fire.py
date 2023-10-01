fire_cell = input().split('#')
water = int(input())
extinguished_cells = []
effort = 0

for fires in fire_cell:
    fire_data = fires.split(' = ')
    type_of_fire = fire_data[0]
    value_of_cell = int(fire_data[1])

    max_fire = 0
    min_fire = 0

    if type_of_fire == 'High':
        max_fire = 125
        min_fire = 81
    elif type_of_fire == 'Medium':
        max_fire = 80
        min_fire = 51
    elif type_of_fire == 'Low':
        max_fire = 50
        min_fire = 1

    if min_fire <= value_of_cell <= max_fire:
        if water < value_of_cell:
            continue
        else:
            water -= value_of_cell
            effort += value_of_cell / 4
            extinguished_cells.append(value_of_cell)
    else:
        continue


print('Cells:')
for cell in extinguished_cells:
    print(f'- {cell}')


total_fire = sum(extinguished_cells)
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')