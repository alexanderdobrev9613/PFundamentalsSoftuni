import re

text_string = input()
pattern = r"([|#])([a-zA-Z ]+)\1([\d]{2}\/[\d]{2}\/[\d]{2})\1([\d]{1,5})\1"
food_data = re.findall(pattern, text_string)
daily_calories = 2000
total_calories = 0
for i in food_data:
    food_type, exp_date, calories = i[1], i[2], i[3]
    total_calories += int(calories)

days_with_food = total_calories // daily_calories
print(f'You have food to last you for: {days_with_food} days!')
for food in food_data:
    food_type, exp_date, calories = food[1], food[2], food[3]
    print(f"Item: {food_type}, Best before: {exp_date}, Nutrition: {calories}")