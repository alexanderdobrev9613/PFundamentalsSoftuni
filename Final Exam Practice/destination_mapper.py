import re

string = input()
travel_points = 0
pattern = r"([=\/])([A-Z][a-zA-Z]{2,})\1"
destination_list = re.findall(pattern, string)
print(destination_list)
exit()
valid_destination_list = [match[1] for match in destination_list]
for current_destination in valid_destination_list:
    travel_points += len(current_destination)

print(f"Destinations: {', '.join(valid_destination_list)}")
print(f"Travel Points: {travel_points}")