import re

main_pattern = r"([\*:]{2})([A-Z][a-z]{2,})\1"
input_str = input()
input_digit_pattern = r"\d"
list_of_cool_emojis = []
whole_emoji = ""

#Cool threshold:
cool_threshold = re.findall(input_digit_pattern, input_str)
result = 1
for digit in cool_threshold:
    result *= int(digit)
cool_threshold = result

emojis = re.findall(main_pattern, input_str)
count_of_valid_emojis = len(emojis)

for i in emojis:
    clean_emoji = i[1]
    coolness = 0
    for char in clean_emoji:
        coolness += ord(char)
    if i[0] == "::":
        whole_emoji = f'::{clean_emoji}::'
        list_of_cool_emojis.append(whole_emoji)
    elif i[0] == "**":
        whole_emoji = f'**{clean_emoji}**'
        list_of_cool_emojis.append(whole_emoji)
    if coolness <= cool_threshold:
        list_of_cool_emojis.remove(whole_emoji)

print(f'Cool threshold: {cool_threshold}')
print(f'{count_of_valid_emojis} emojis found in the text. The cool ones are:')
for i in list_of_cool_emojis:
    print(i)

