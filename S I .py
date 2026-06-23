class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"

    def display(self):
        print(f"\nRoll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Marks   : {self.marks}")
        print(f"Grade   : {self.calculate_grade()}")


students = {}


def add_student():
    roll_no = int(input("Enter Roll Number: "))

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    students[roll_no] = Student(roll_no, name, marks)
    print("Student Added Successfully!")


def view_students():
    if not students:
        print("No students found!")
        return

    for student in students.values():
        student.display()


def search_student():
    roll_no = int(input("Enter Roll Number: "))

    if roll_no in students:
        students[roll_no].display()
    else:
        print("Student not found!")


def update_marks():
    roll_no = int(input("Enter Roll Number: "))

    if roll_no in students:
        new_marks = float(input("Enter New Marks: "))
        students[roll_no].marks = new_marks
        print("Marks Updated Successfully!")
    else:
        print("Student not found!")


def delete_student():
    roll_no = int(input("Enter Roll Number: "))

    if roll_no in students:
        del students[roll_no]
        print("Student Deleted Successfully!")
    else:
        print("Student not found!")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")