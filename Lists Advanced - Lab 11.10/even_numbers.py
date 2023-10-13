numies = list(map(int, input().split(', ')))
index_list = []
index = 0

for num in numies:
    if num % 2 == 0:
        index_list.append(index)
    index += 1

print(index_list)


"""ili
numies = list(map(int, input().split(', ')))
found_indices = map(lambda x: x if numies[x] % 2 == 0 else 'no', range(len(numies)))

even_indices = list(filter(lambda a: a != 'no', found_indices))

print(even_indices)
"""