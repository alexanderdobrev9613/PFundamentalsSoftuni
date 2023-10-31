from math import ceil

budget = float(input())
students = int(input())
package_flour_price = float(input())
egg_price = float(input())
apron_price = float(input())
counter = 0
total_price = 0

for set in range(students):
    total_price += package_flour_price + 10 * egg_price
    counter += 1
    if counter % 5 == 0:
        total_price -= package_flour_price

price_of_aprons = students * apron_price + ceil((students / 5)) * apron_price
total_price += price_of_aprons
difference = abs(budget - total_price)

if total_price <= budget:
    print(f'Items purchased for {total_price:.2f}$.')
else:
    print(f'{difference:.2f}$ more needed.')