def encoder(code):
    estr = ''
    for i in range(0, len(code)):
        digit = int(code[i])
        digit += 3
        if digit > 9:
            digit %= 10
        estr += str(digit)
    return estr

def decoder(encoded_pass):
    dstr = ''
    for i in range(0, len(encoded_pass)):
        digit = int(encoded_pass[i])
        digit -= 3
        if digit < 0:
            digit += 10
            dstr += str(digit)
        else:
            dstr += str(digit)
    return dstr


def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")

if __name__ == '__main__':
    menu()
    choice = input("Please enter an option: ")
    while True:
        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded = encoder(password)
            print(encoder(password))
            print("\nYour password has been encoded and stored!\n")
            menu()
            choice = input("Please enter an option: ")

        if choice == "2":
            print(f"The encoded password is {encoded}, and the original password is {decoder(encoded)}.")
            menu()
            choice = input("Please enter an option: ")

        if choice == "3":
            break
