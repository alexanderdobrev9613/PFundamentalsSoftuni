first_sequence = input().split(', ')
second_sequence = input().split(', ')


matching_list = [element1 for element1 in first_sequence if any(element1 in element2 for element2 in second_sequence)]


print(matching_list)