#Dictionaries

monthconversions={
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
}
print(monthconversions["Jan"])
print(monthconversions.get("Jan"))
print(monthconversions.get("Feb","Not a valid key"))
print(monthconversions.get("dec","Not a valid key"))


#While loops

i=1
while i<=10:
    print(i)
    i+=1
print("Done with loop")

# Building a guessing game

secret_word="Apple"
guess=""

while guess!=secret_word:
    guess=input("Enter your guess: ")
print("You win!")

# Building better guessing game

secret_word="Apple"
guess=""
guess_count=0
guess_limit=3
out_of_guesses=False

while guess!=secret_word and not(out_of_guesses):
    if guess_count<guess_limit:
        guess=input("Enter your guess: ")
        guess_count+=1
    else:
        out_of_guesses=True

if out_of_guesses:
    print("Out of guesses, you lose!")
else:
    print("You win!")


#For loops

for letter in "Apple":
    print(letter)

friends=["John","Mike","Mary"]
for friend in friends:
    print(friend)

for index in range(10):
    print(index)

for index in range(3,10):
    print(index)

for index in range(len(friends)):
    print(friends[index])