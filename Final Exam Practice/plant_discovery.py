num = int(input())
plants_for_exhibition = []

for i in range(num):
    plant_info = input().split("<->")
    name, rarity = plant_info[0], plant_info[1]
    plant = {'name': name, 'rarity': rarity, 'rating': 0}
    plants_for_exhibition.append(plant)

while True:
    command = input().split(': ')
    if command[0] == 'Exhibition':
        print('Plants for the exhibition:')
        for plant in plants_for_exhibition:
            print(f"- {plant['name']}; Rarity: {plant['rarity']}; Rating: {plant['rating']:.2f}")
        break
    elif command[0] == 'Rate':
        info = command[1].split(' - ')
        plant_name, plant_rating = info[0], int(info[1])
        plant_found = False
        for plant in plants_for_exhibition:
            if plant['name'] == plant_name:
                plant_found = True
                if plant['rating'] != 0:
                    plant['rating'] = (plant['rating'] + plant_rating) / 2
                else:
                    plant['rating'] += plant_rating
        if not plant_found:
            print('error')
    elif command[0] == 'Update':
        info = command[1].split(' - ')
        plant_name, new_rarity = info[0], info[1]
        plant_found = False
        for plant in plants_for_exhibition:
            if plant['name'] == plant_name:
                plant_found = True
                plant['rarity'] = new_rarity
        if not plant_found:
            print('error')
    elif command[0] == 'Reset':
        plant_name = command[1]
        plant_found = False
        for plant in plants_for_exhibition:
            if plant['name'] == plant_name:
                plant_found = True
                plant['rating'] = 0
        if not plant_found:
            print('error')



