quantity_of_decorations = int(input())
remaining_days = int(input())
ornament_set_price = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
total_cost = 0
total_spirit = 0
for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2 # cut-nah ot 26ti red i slojih v nachaloto
    if current_day % 2 == 0:
        total_cost += quantity_of_decorations * ornament_set_price
        total_spirit += 5
    if current_day % 3 == 0: #ne e elif za da ne suvpadnat naprimer 3,6,12,etc
        total_cost += quantity_of_decorations * (tree_skirt + tree_garland)
        total_spirit += 10 + 3
    if current_day % 5 == 0:
        total_cost += quantity_of_decorations * tree_lights
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt + tree_lights + tree_garland
if remaining_days % 10 == 0:
    total_spirit -= 30
print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')

