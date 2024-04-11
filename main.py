def encoder(code):
    for i in range(0, len(code)):
        digit = int(i)
        digit += 3
        if digit > 9:
            digit %= 10
        print(digit, end=" ")

def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")

if __name__ == '__main__':
    menu()
    choice = input("Please enter an option: ")
    if choice == "1":
        password = input("Please enter your password to ancode: ")
        encoded_pass = encoder(password)
        print("Your password has been encoded and stored!")
    if choice == "2":
        print(f"The encoded password is {encoded_pass}, and the original password is {password}.")
