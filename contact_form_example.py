
address_book = {}
def add_contact():
    name = input('Enter the name: ')
    phone = input('Enter the phone number: ')
    address = input('Enter the address: ')
    address_book[name] = {'Phone': phone, 'Address': address}
    print(f'Contact {name} has been added!')

def view_contact():
    if not address_book:
        print(f'Address book is empty.')
    else:
        for name, details in address_book.items():
            print(f'Name: {name}')
            print(f"Phone: {details['Phone']}")
            print(f"Address: {details['Address']}")
            print()

def search_contact():
    name = input('Enter the name to search for: ')
    if name in address_book:
        details = address_book[name]
        print(f'Name {name}')
        print(f"Phone: {details['Phone']}")
        print(f"Address: {details['Address']}")
    else:
        print(f'Contact {name} not found in the address book.')

while True:
    print('\nAddress Book Menu:')
    print('1. Add Contact')
    print('2. View Contacts')
    print('3. Search Contact')
    print('4. Exit')

    choice = input('Enter your choiuce (1/2/3/4): ')

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Please select 1,2,3 or 4')
        continue
