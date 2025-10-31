import random

top_of_range = input("Type a number to set the upper limit of the range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time.")
        quit()
else:
    print("Please enter a valid number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess :")
    break
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a valid number next time.")
        continue

    if user_guess == random_number:
        print("Congratulations! You guessed the number.")
        break
    elif user_guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

print("You got it in " + str(guesses) + " guesses!")
