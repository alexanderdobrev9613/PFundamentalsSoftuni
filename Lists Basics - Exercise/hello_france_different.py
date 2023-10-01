items_input = input().split('|')
budget = float(input())
bought_items = []
total_profit = 0

for item_str in items_input:
    item_data = item_str.split('->')
    item_type = item_data[0]
    price = float(item_data[1])

    if budget >= price:
        max_price = 0
        if item_type == 'Clothes':
            max_price = 50.00
        elif item_type == 'Shoes':
            max_price = 35.00
        elif item_type == 'Accessories':
            max_price = 20.50

        if price <= max_price:
            budget -= price
            formatted_price = '{:.2f}'.format(price * 1.40) #zashto da ne stane taka?
            new_price = float(formatted_price)
            total_profit += new_price - price
            bought_items.append(new_price)

for i in bought_items: #i taka?
    print(i, end=' ')
print()
print(f"Profit: {total_profit:.2f}")
total_budget = sum(bought_items) + budget

if total_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")