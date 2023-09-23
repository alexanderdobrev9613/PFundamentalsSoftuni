number_of_lines = int(input())
water_counter = 0
tank_capacity = 255
for line in range(number_of_lines):
    water_litres = int(input())
    if tank_capacity - water_litres < 0:
        print('Insufficient capacity!')
        continue
    tank_capacity -= water_litres
    water_counter += water_litres
print(water_counter)