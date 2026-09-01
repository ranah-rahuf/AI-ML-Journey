import display_utils

while True:

    print("Student Management Utility")

    print("1. Enter Student : ")
    print("2. Exit : ")

    try:
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        name = input("Enter your name : ")

        try:
            subjects = int(input("Enter number of subjects : "))
            if subjects <= 0:
                print("Number of subjects must be a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        marks = []
        valid=True

        for i in range(subjects):
            try:
                mark = int(input(f"Enter mark {i+1}: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                valid=False
                break

            if mark < 0 or mark > 100:
                print("Marks should be between 0 and 100.")
                valid=False
                break

            marks.append(mark)
        if not valid:
            continue
        display_utils.display_student(name, marks)
        

    elif choice == 2:
        print("Exiting the program")
        break
    else:
        print("Invalid choice. Please try again.")
