key = int(input())
symbols = int(input())
message = ''

for character in range(1, symbols + 1):
    letter = input()
    new_letter = ord(letter) + key
    message += chr(new_letter)

print(message)