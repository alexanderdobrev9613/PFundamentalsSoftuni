def calculate_total_price(product, quantity):
    if product == 'coffee':
        return f'{1.5 * quantity:.2f}'
    elif product == 'coke':
        return f'{1.4 * quantity:.2f}'
    elif product == 'water':
        return f'{1 * quantity:.2f}'
    elif product == 'snacks':
        return f'{2 * quantity:.2f}'

product = input()
quantity = int(input())
result = calculate_total_price(product, quantity)
print(result)