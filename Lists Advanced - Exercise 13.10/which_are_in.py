first_sequence = input().split(', ')
second_sequence = input().split(', ')

def element_match():
    matching_list = []
    for element1 in first_sequence:
        for element2 in second_sequence:
            if element1 in element2 and element1 not in matching_list:
                matching_list.append(element1)
    result = matching_list
    return result

print(element_match())