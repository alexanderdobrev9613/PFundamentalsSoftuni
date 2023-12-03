stops = input()

while True:
    command = input().split(':')
    if command[0] == 'Travel':
        print(f"Ready for world tour! Planned stops: {stops}")
        break
    elif command[0] == 'Add Stop':
        index, string = int(command[1]), command[2]
        if index < len(stops):
            stops = stops[:index] + string + stops[index:]
        print(stops)
    elif command[0] == 'Remove Stop':
        start_index, end_index = int(command[1]), int(command[2])
        if start_index < len(stops) and end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1:]
        print(stops)
    elif command[0] == 'Switch':
        old_string, new_string = command[1], command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)



