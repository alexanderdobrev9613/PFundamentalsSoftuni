lost_battles = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_helmet = lost_battles // 2
total_sword = lost_battles // 3
total_shield = lost_battles // (2 * 3)
total_armor = total_shield // 2

expenses = total_helmet * helmet_price\
           + total_sword * sword_price\
           + total_shield * shield_price\
           + total_armor * armor_price
print(f'Gladiator expenses: {expenses:.2f} aureus')