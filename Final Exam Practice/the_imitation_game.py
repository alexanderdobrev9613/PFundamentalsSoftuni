encrypted_message = input()

while True:
    command = input()
    if command == 'Decode':
        break
    current_command = command.split('|')
    action, first_symbol = current_command[0], current_command[1]
    if action == 'Move':
        first_symbol = int(first_symbol)
        encrypted_message = encrypted_message[first_symbol:] + encrypted_message[:first_symbol]
    elif action == 'Insert':
        first_symbol = int(first_symbol)
        encrypted_message = encrypted_message[:first_symbol] + current_command[2] + encrypted_message[first_symbol:]
    elif action == 'ChangeAll':
        encrypted_message = encrypted_message.replace(first_symbol, current_command[2])

print(f"The decrypted message is: {encrypted_message}")