strings = input().split()
n = int(input())
list_of_int_numbers = []
counter = 0

for i in strings:
    list_of_int_numbers.append(int(i))

for _ in range(n):
    list_of_int_numbers.remove(min(list_of_int_numbers))

for i in range(len(list_of_int_numbers)):
    list_of_int_numbers[i] = str(list_of_int_numbers[i])

print(', '.join(list_of_int_numbers))