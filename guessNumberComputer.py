import random

print("Computer guessing number game")


def guess(low, high):
    print(f"Range is between {low} and {high}")
    guide = 'x'
    random_num = random.randint(low, high+1)
    while guide != 'y':
        print(f"computer guess: {random_num}")
        guide = input("Is the computer guess correct? yes=y, high=h, low=l: ")
        if guide == 'h':
            high = random_num+1
            random_num = random.randint(low, high)
        elif guide == 'l':
            low = random_num+1
            random_num = random.randint(low, high)
        elif guide == 'y':
            print("The computer guided correctly")
        else:
            print("Invalid answer")


def range():
    low = int(input("Enter the lowest number of your range: "))
    high = int(input("Enter the highest number of your range: "))
    guess(low, high)


range()
