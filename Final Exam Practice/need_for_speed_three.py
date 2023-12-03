car_count = int(input())
cars_in_possession = []

for i in range(car_count):
    current_car = input().split('|')
    name, mileage, fuel = current_car[0], int(current_car[1]), int(current_car[2])
    car = {'name': name, 'mileage': mileage, 'fuel': fuel}
    cars_in_possession.append(car)

while True:
    command = input().split(' : ')
    if command[0] == 'Stop':
        for car in cars_in_possession:
            print(f"{car['name']} -> Mileage: {car['mileage']} kms, Fuel in the tank: {car['fuel']} lt.")
        break
    elif command[0] == 'Drive':
        vehicle, distance, needed_fuel = command[1], int(command[2]), int(command[3])
        for car in cars_in_possession:
            if car['name'] == vehicle:
                if needed_fuel > car['fuel']:
                    print('Not enough fuel to make that ride')
                else:
                    car['mileage'] += distance
                    car['fuel'] -= needed_fuel
                    print(f"{vehicle} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
                if car['mileage'] >= 100000:
                    cars_in_possession.remove(car)
                    print(f"Time to sell the {vehicle}!")
    elif command[0] == 'Refuel':
        vehicle, refuel_amount = command[1], int(command[2])
        for car in cars_in_possession:
            if car['name'] == vehicle:
                max_fuel = 75
                fuel_to_add = min(refuel_amount, max_fuel - car['fuel'])
                car['fuel'] += fuel_to_add
                print(f"{vehicle} refueled with {fuel_to_add} liters")
    elif command[0] == 'Revert':
        vehicle, kilometers = command[1], int(command[2])
        for car in cars_in_possession:
            if car['name'] == vehicle:
                car['mileage'] -= kilometers
                if car['mileage'] < 10000:
                    car['mileage'] = 10000
                else:
                    print(f'{vehicle} mileage decreased by {kilometers} kilometers')