# 1.Matrix

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[1][1])

# 2.Nested loop

for row in matrix:
    for column in row:
        print(column)

# 3. Nested loop

for i in range(3):
    for j in range(5):
        print("*",end="")
    print()

# 4. Power function

def powerfunction(base,pow):
    result=1
    for index in range(pow):
        result =result*base
    return result
print(powerfunction(2,5))

# 5. For loop
for i in range(10,0,-1):
 print(i)

