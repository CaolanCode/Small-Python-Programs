import random


def user_choice():
    choice = input("Rock = r, Paper = p, Scissors = s: ")
    computer_choice(choice)


def computer_choice(user):
    options = ['r', 'p', 's']
    choice = random.choice(options)
    if user == choice:
        print(f"The computer is {choice}")
        print("Draw")
    elif user == 'p' and choice == 'r':
        print("The computer is Rock")
        print("You win!")
    elif user == 'r' and choice == 'p':
        print("The computer is Paper")
        print("The computer wins!")
    elif user == 's' and choice == 'p':
        print("The computer is Paper")
        print("You win!")
    elif user == 'p' and choice == 's':
        print("The computer is Scissors")
        print("The computer wins!")
    elif user == 'r' and choice == 's':
        print("The computer is Scissors")
        print("You win!")
    elif user == 's' and choice == 'r':
        print("The computer is Rock")
        print("The computer wins!")
    else:
        print("Invalid entry")


user_choice()
