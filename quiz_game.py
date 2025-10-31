print("Welcome to the Quiz Game!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Great! Let's start the game.")
score = 0

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Paris.")

answer = input ("What is 5 + 7? ")
if answer.lower() == "12":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 12.")

answer = input("What is the largest planet in our solar system? ")
if answer.lower() == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Jupiter.")

print("you got " + str(score) + " questions correct!")
print("You got " + str((score / 3) * 100) + "%.")