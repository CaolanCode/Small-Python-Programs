import random
import string


def create_password():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    punctuation = list(string.punctuation)
    length = int(input("Enter the length of the password: "))
    counter = 0
    password = ""
    while counter < length:
        choice = random.randint(1, 3)
        counter += 1
        if choice == 1:
            password += random.choice(letters)
        elif choice == 2:
            password += random.choice(numbers)
        elif choice == 3:
            password += random.choice(punctuation)

    return password


print(create_password())
