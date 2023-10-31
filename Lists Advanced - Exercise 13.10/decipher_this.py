#ascii / index swapping / is_digit ili is_numeric

secret_message = input().split()
deciphered_message = []
help_words = []
for words in secret_message:
    ascii_char = ''
    for word in words:
        if word.isdigit():
            ascii_char += word
        else:
            help_words.append(word)

    first_char = chr(int(ascii_char))
    help_words[-1], help_words[0] = help_words[0], help_words[-1]
    help_words.insert(0, first_char)
    deciphered_word = ''.join(help_words)
    help_words = []
    deciphered_message.append(deciphered_word)

result = ' '.join(deciphered_message)
print(result)