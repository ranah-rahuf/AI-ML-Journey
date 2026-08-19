# STRINGS:

# 1. Reverse a string
word="Apple"
reverse=""
for index in word:
    reverse=index + reverse
print(reverse)

# 2. Count vowels
word="Apple"
count=0

for index in word:
    if index in "AEIOUaeiou":
        count +=1
print(count)


# 3. Check palindrome
word="malayalam"
reverse=""
for index in word:
    reverse=index + reverse
if reverse==word:
    print("palindrome")
else:
    print("not palindrome")


# 4. Count words
sentence="this is a python program"
if sentence:
    count = 1
else:
    count = 0
for words in sentence:
    if words==" ":
        count+=1
print(count)

# 5. Remove duplicate characters
word="applepiece"
result=""
for index in range(len(word)):
    if word[index] not in result:
        result+=word[index]
print(result)

#5.cleaner version
word="applepiece"
for letter in word:
    if letter not in result:
        result += letter
print(result)

#6.Count Uppercase letters:
word="HeLLo PYthon"
count=0
for letter in word:
    if letter.isupper():
        count+=1
print(count)

# 7.Find the fist non repeating character
word="aabbcdde"
for letter in word:
    if word.count(letter)==1:
        print(letter)
        break

# 8.Check whether two strings are anagrams.
string1="listen"
string2="silent"

if sorted(string1)==sorted(string2):
    print("Anagrams")
else:
    print("Not Anagrams")

# 9.Print vowels only 
word = "python programming"
for letter in word:
    if letter in "aeiouAEIOU":
        print(letter,end="")

# 9.better version

word = "python programming"
vowels = ""

for letter in word:
    if letter in "aeiouAEIOU":
        vowels += letter

print(vowels)

# 10.Print vowels, consonants, and spaces separately
word = "python programming"
vowels = 0
consonants = 0
spaces = 0

for letter in word:
    if letter in "aeiouAEIOU":
        vowels += 1
    elif letter == " ":
        spaces += 1
    elif letter.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)

#11.Without using .upper() or .lower() ,swap the case of every letter

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

word = "PyThOn"

result = ""

for letter in word:

    if letter in upper:
        index = upper.index(letter)
        result += lower[index]

    elif letter in lower:
        index = lower.index(letter)
        result += upper[index]

print(result)

# 11. Using function:
word = "PyThOn"

print(word.swapcase())

# 12. Count letters:
word="Mississippi"
finalword=""
for letter in word:
    if letter not in finalword:
      finalword+=letter
      count=word.count(letter)
      print(f"{letter}: {count}")
