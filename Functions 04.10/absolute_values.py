number_list = input().split()
absolute_values = []

for n in number_list:
    absolute_values.append(abs(float(n)))

print(absolute_values)