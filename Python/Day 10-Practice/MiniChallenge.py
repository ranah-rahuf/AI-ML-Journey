print("=====Safe Calculator=====")
while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice : "))
        if choice < 1 or choice > 5:
            raise ValueError("Invalid choice! Please select a valid option.")
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 + num2
            print("Result:", result)
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == 2:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 - num2
            print("Result:", result)
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == 3:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 * num2
            print("Result:", result)
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == 4:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 / num2
            print("Result:", result)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except ZeroDivisionError:
            print("Cannot divide by zero!")

    elif choice == 5:
        print("Exiting the calculator!")
        break

    