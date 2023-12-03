import re
string = input()

pattern = r"([@#]+)([a-z]{3,})([@#]+)([^a-zA-Z0-9]*)([\/]+)([0-9]+)([\/]+)"
eggs = re.findall(pattern, string)
for egg in eggs:
    color, amount = egg[1], egg[5]
    print(f'You found {amount} {color} eggs!')
