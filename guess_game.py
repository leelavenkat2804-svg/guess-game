import random

number = random.randint(1, 10)
attempts = 3

print("🎯 Number Guessing Game")
print("Guess a number between 1 and 10")
print("You have 3 attempts!")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 Correct! You won!")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

    attempts -= 1
    print("Attempts left:", attempts)

if attempts == 0:
    print("😢 Game over!")
    print("The number was:", number)
