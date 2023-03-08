# Jamison McDivitt (Says to print name at top of file with encode function)

# Prints Menu selection
def menu():
    print('Menu\n--------')
    print('1. Encode\n2. Decode\n3. Quit\n')


# Encodes the user inputed string
def encode(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


# Decodes the user inputed string
def decoder(password):
    pass


def main():

    run_program = True

    while run_program:
        menu()

        user_selection = int(input('Please select a menu option: '))

        if user_selection == 1:
            while True:
                user_password = input('\nPlease enter your 8-digit password to encode: ')
                if len(user_password) != 8:
                    print('\nPassword must be 8-digits!')
                else:
                    encoded_password = encode(user_password)
                    print(f'\nEncoded password: {encoded_password}\n')
                    break
            continue

        elif user_selection == 2:
            user_password = input('\nPlease enter a password to encode: ')
            decoded_password = decode(user_password)
            print(f'\nDecoded password: {decoded_password}')
            continue

        elif user_selection == 3:
            print('\nGoodbye!')
            run_program = False
        else:
            print('Not a valid selection. Please select a new menu option')
            continue


if __name__ == "__main__":
    main()