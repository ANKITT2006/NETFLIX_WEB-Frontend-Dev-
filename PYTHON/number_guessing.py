import random

print("Welcome User")
print("Guess the number between 1 and 20")

# set the range
lower = 1
upper = 20

# computer picks a random number
secret_number = random.randrange(lower, upper)

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < lower or guess > upper:
        print("Please guess within the range!")
    elif guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it right ")
        print("Number of attempts:", attempts)
        break
