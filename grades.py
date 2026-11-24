print("Welcome to Grade Calculator")

mark = int(input("Enter student mark: "))

if mark < 0 or mark > 100:
    print("Invalid mark")
else:
    if mark >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")

    if mark >= 80:
        print("Grade: A")
    elif mark >= 60:
        print("Grade: B")
    else:
        print("Grade: C")