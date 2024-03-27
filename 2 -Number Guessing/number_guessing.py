import random


guess = input("Please enter a number (0-10): ")


pc = random.randrange(11)
print("Computer's number: ", int(pc))
print("Your guess", guess)

if pc == int(guess):
    print("Correct answer!")
else:
    print("Wrong!")