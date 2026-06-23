class Student:

    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        student = Student(sid, name, marks)
        students.append(student)

    elif choice == "2":
        for student in students:
            student.display()
            print("-" * 20)

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")