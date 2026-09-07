file = open("student.txt", "a")

def add_student():
    student_id = input("Student ID: ")
    student_name = input("Student Name: ")
    age = input("Age: ")
    course = input("Course: ")

    try:
        with open("student.txt", "a") as file1:
            file1.write(f"{student_id} | {student_name} | {age} | {course}\n")
            print("Student added successfully")

    except FileNotFoundError:
        print("File not found")


def view_students():
    print("\nStudent Records")

    try:
        with open("student.txt", "r") as file2:
            students = file2.read()

            if students:
                print(students)
            else:
                print("No student records found")

    except FileNotFoundError:
        print("File not found")
        print("The file does not exist yet")

def search_student():
    print("\n--- Search Student ---")
    student_id = input("Enter Student ID: ")

    try:
        with open("student.txt", "r") as file:
            found = False

            for student in file:
                if student_id in student:
                    print("\nStudent Found:")
                    print(student)
                    found = True

            if not found:
                print("Student not found")

    except FileNotFoundError:
        print("File not found")
        print("The file does not exist yet")

def main():
    while True:
        print("\nSTUDENT MANAGEMENT")
        print("1. Add Student")
        print("2. View")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
main()