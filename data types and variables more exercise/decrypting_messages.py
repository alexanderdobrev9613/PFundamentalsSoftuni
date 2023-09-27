key = int(input())
symbols = int(input())
message = []

for character in range(1, symbols + 1):
    letter = input()
    new_letter = ord(letter) + key
    message.append(chr(new_letter))

for item in message:
    print(item, end='')