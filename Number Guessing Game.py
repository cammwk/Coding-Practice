import random

guess = ""
secretNumber = random.randint(1, 100)
attempts = 0
correct = False

while not correct:
    try:
        guess = int(input("Guess a number 1-100: "))
    except ValueError:
            print("Please enter a valid number.")
            continue

    attempts += 1

    if guess == secretNumber:
        print(f"Congratulations you got the answer in {attempts} attempts.")
        correct = True
    else:
        print(f"{guess} is incorrect, try again.")
        correct = False
