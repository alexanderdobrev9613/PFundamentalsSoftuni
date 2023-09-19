# 1 bread: 1 eggs pack / 1kg flour / 0.250ml milk

budget = float(input())
kg_flour_price = float(input())
eggs_pack_price = kg_flour_price * 0.75
litre_milk_price = (0.25 * kg_flour_price) + kg_flour_price
one_bread_price = eggs_pack_price + kg_flour_price + (litre_milk_price / 4)
total_breads_price = 0
counter = 0
colored_eggs = 0

while budget > one_bread_price:
    counter += 1
    colored_eggs += 3
    total_breads_price += one_bread_price
    budget -= one_bread_price
    if counter % 3 == 0:
        colored_eggs -= (counter - 2)

print(f'You made {counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')

