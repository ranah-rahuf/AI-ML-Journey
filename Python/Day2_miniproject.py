# Favourite Movies Manager

movies = []
print("Enter 5 favourite movies:")
movies.append(input("1. "))
movies.append(input("2. "))
movies.append(input("3. "))
movies.append(input("4. "))
movies.append(input("5. "))

print("\nYour favourite movies")

print("1. "+movies[0])
print("2. "+movies[1])
print("3. "+movies[2])
print("4. "+movies[3])
print("5. "+movies[4])

replace=int(input("enter a movie number to replace: "))
movies[replace-1] = input("enter the new movie name: ")

print("\nUpdated favourite movies")

print("1. "+movies[0])
print("2. "+movies[1])
print("3. "+movies[2])
print("4. "+movies[3])
print("5. "+movies[4])
