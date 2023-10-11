def all_the_characters(first, second) -> list:
    characters = []
    for current_char_as_digit in range(ord(first) + 1, ord(second)):
        characters.append(chr(current_char_as_digit))
    return characters


first_character = input()
second_character = input()
final_result = all_the_characters(first_character, second_character)
print(' '.join(final_result))