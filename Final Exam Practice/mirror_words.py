import re

text_string = input()
pattern = r"([@#])([A-Za-z]{3,})\1"
words = []
matching_words = []

matches = re.findall(pattern, text_string)
for element in matches:
    word = element[1]
    words.append(word)

for word in words:
    reversed_word = word[::-1]
    if reversed_word in words:
        matching_words.append(word)
        matching_words.append(reversed_word)

if len(matches) == 0:
    print('No word pairs found!')
else:
    print(f'{len(matches)} word pairs found!')
if len(matching_words) > 0:
    print('The mirror words are:')
    print(' <=> '.join(matching_words))
else:
    print(f'No mirror words!')