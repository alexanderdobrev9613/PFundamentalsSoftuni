import re

participants = input().split(', ')
text = input()
pattern_name = r"[A-Za-z]"
pattern_distance = r"\d"
current_distance = 0
first_dict = {}

while text != 'end of race':
    name_list = re.findall(pattern_name, text)
    name = ''.join(name_list)
    distance_list = re.findall(pattern_distance, text)
    distance = sum(map(int, distance_list))
    if name in participants:
        current_distance += distance
        first_dict += {name: current_distance}
    text = input()