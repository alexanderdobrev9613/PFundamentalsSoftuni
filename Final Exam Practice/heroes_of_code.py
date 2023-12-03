number_of_heroes = int(input())
heroes_list = []

for i in range(number_of_heroes):
    current_hero = input().split()
    hero_name, hp, mp = current_hero[0], int(current_hero[1]), int(current_hero[2])
    hero = {'name': hero_name, 'hp': hp, 'mp': mp}
    heroes_list.append(hero)

while True:
    command = input().split(' - ')
    if command[0] == 'End':
        break
    elif command[0] == 'CastSpell':
        name, mp_needed, spell_name = command[1], int(command[2]), command[3]
        for hero in heroes_list:
            if hero['name'] == name:
                if hero['mp'] >= mp_needed:
                    hero['mp'] -= mp_needed
                    print(f"{name} has successfully cast {spell_name} and now has {hero['mp']} MP!")
                else:
                    print(f"{name} does not have enough MP to cast {spell_name}!")

    elif command[0] == 'TakeDamage':
        name, damage, attacker = command[1], int(command[2]), command[3]
        for hero in heroes_list:
            if hero['name'] == name:
                hero['hp'] -= damage
                if hero['hp'] > 0:
                    print(f"{name} was hit for {damage} HP by {attacker} and now has {hero['hp']} HP left!")
                else:
                    heroes_list.remove(hero)
                    print(f"{name} has been killed by {attacker}!")

    elif command[0] == 'Recharge':
        name, amount = command[1], int(command[2])
        for hero in heroes_list:
            if hero['name'] == name:
                max_mp = 200
                mp_to_add = min(amount, max_mp - hero['mp'])
                hero['mp'] += mp_to_add
                print(f"{name} recharged for {mp_to_add} MP!")
    elif command[0] == 'Heal':
        name, amount = command[1], int(command[2])
        for hero in heroes_list:
            if hero['name'] == name:
                max_hp = 100
                hp_to_add = min(amount, max_hp - hero['hp'])
                hero['hp'] += hp_to_add
                print(f"{name} healed for {hp_to_add} HP!")

for hero in heroes_list:
    print(f"{hero['name']}")
    print(f" HP: {hero['hp']}")
    print(f" MP: {hero['mp']}")