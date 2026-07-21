#Exponent function

print(2**3)

def raise_to_power(base_num,pow_num):
    result=1
    for index in range(pow_num):
        result=result*base_num
    return(result)
print(raise_to_power(2,3))

#2D Lists and nested Loop:

number_grid=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][2])

for row in number_grid:
    print(row)

for row in number_grid:
    for column in row:
        print(column)

#Build a translator:

def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation=translation + "g"
        else:
            translation=translation + letter
    return translation

print(translate(input("Enter phrase: ")))

#2
def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation=translation + "G"
            else:
                translation=translation + "g"
        else:
            translation=translation + letter
    return translation

print(translate(input("Enter phrase: ")))

'''
gflfdgmkgmklmghh
'''