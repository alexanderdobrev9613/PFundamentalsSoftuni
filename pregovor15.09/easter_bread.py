# 1 bread: 1 eggs pack / 1kg flour / 0.250ml milk

budget = float(input())
kg_flour_price = float(input())
eggs_pack_price = kg_flour_price * 0.75
litre_milk_price = (0.25 * kg_flour_price) + kg_flour_price
one_bread_price = eggs_pack_price + kg_flour_price + (litre_milk_price / 4)
total_breads_price = one_bread_price
counter = 1
colored_eggs = 3

while budget > total_breads_price:
    total_breads_price += one_bread_price
    counter += 1
    colored_eggs += 3
    if counter % 3 == 0:
        colored_eggs -= (counter - 2)
diff = budget - total_breads_price
print(f'You made {counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {diff:.2f}BGN left.')

