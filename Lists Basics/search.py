n = int(input())
word = input()
first_list = []

for strings in range(n):
    current_string = input()
    first_list.append(current_string)


print(first_list)

for element in range(len(first_list)-1, -1, -1):
    if word not in first_list[element]:
        first_list.remove(first_list[element])
print(first_list)