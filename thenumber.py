import random

secret_number = random.randint(1,20)

for i in range(1,7):
    print("take a guess")
    guess = int(input())

    if guess < secret_number:
        print("Sua adivinhação é menor do que")
    elif guess > secret_number:
        print("Sua adivinhação é maior do que")
    else:
        print("yes you hit that")