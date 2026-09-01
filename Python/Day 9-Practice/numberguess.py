import random
number=random.randint(1, 10)

for i in range(3):
    guess=int(input("Guess The Number : "))
    if guess == number:
        print("Correct")
        break
    else:
        print("You are guessed a Wrong number!")


