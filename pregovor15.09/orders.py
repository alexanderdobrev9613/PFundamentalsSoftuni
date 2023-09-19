number_of_orders = int(input())
total = 0

for current_order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    price = price_per_capsule * days * capsules_needed_per_day
    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_needed_per_day <= 2000:
        total += price
        print(f'The price for the coffee is: ${price:.2f}')
    else:
        continue
print(f'Total: ${total:.2f}')
