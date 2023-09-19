first_string = input()
second_string = input()
last_printed_string = first_string
for character_index in range(len(first_string)): #ili len(second_string) nqma znachenie zashtoto sa ednakvi
    left_part = second_string[:character_index + 1] #ili [0:character_index + 1]
    right_part = first_string[character_index + 1:] # seled kato e prazno sled : znachi "do kraq"
    new_string = left_part + right_part
    if new_string != last_printed_string:
        print(new_string)
        last_printed_string = new_string