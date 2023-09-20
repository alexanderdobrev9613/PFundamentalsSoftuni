year = int(input())

while True:
    year += 1
    year_as_string = str(year)
    repetition_counter = 1
    for index, digit in enumerate(year_as_string):
        for control_index in range(index + 1, len(year_as_string)):
            if year_as_string[control_index] == digit:
                repetition_counter += 1
                break
            if repetition_counter > 1:
              break
    if repetition_counter == 1:
        break
print(year)