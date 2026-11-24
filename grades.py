print("Student Grade Calculator")

mark = int(input("Enter student mark: "))

if mark < 0 or mark > 100:
    print("Invalid mark")
elif mark >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")