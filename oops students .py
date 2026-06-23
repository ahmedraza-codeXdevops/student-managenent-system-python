class Student:

    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Marks:", self.marks)


# Creating objects
s1 = Student(101, "Ahmed", 85)
s2 = Student(102, "Raza", 92)

# Displaying details
s1.display()
s2.display()