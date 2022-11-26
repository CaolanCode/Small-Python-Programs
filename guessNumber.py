import random

print("Guess the number game")
print("---------------------")

random_num = random.randint(1, 11)
num = 0
print(random_num)

while num != random_num:
    num = int(input("Enter a number between 1 - 10: "))
    if num == random_num:
        print(f"{num} is correct!")
        print(num)
    else:
        print(f"{num} is incorrect")
