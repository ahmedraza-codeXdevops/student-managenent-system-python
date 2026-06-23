class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

    def id_card(self):
        print("----- ID CARD -----")
        print("Roll:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)

s1 = Student(101, "Ahmed", "BCA")
s1.id_card()