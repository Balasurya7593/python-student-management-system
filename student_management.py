class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


students = []


while True:
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")

        student = Student(name, age, grade)
        students.append(student)

        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List:")
            for student in students:
                print(student.name, "-", student.age, "-", student.grade)

    elif choice == "3":
        search_name = input("Enter student name to search: ")

        found = False

        for student in students:
            if student.name.lower() == search_name.lower():
                print("Student Found:")
                print(student.name, "-", student.age, "-", student.grade)
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        delete_name = input("Enter student name to delete: ")

        for student in students:
            if student.name.lower() == delete_name.lower():
                students.remove(student)
                print("Student deleted.")
                break
        else:
            print("Student not found.")

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")