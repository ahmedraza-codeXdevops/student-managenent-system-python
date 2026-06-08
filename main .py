import sqlite3

def connect():
    return sqlite3.connect("student.db")

def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, age, course) VALUES(?,?,?)",
        (name, age, course)
    )

    conn.commit()
    conn.close()

    print("Student Added Successfully!")

def view_students():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("\nStudent Records")
    print("-" * 40)

    for student in students:
        print(student)

    conn.close()

def search_student():
    sid = int(input("Enter Student ID: "))

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (sid,)
    )

    student = cursor.fetchone()

    if student:
        print(student)
    else:
        print("Student Not Found!")

    conn.close()

def delete_student():
    sid = int(input("Enter Student ID to Delete: "))

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (sid,)
    )

    conn.commit()
    conn.close()

    print("Student Deleted Successfully!")

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")