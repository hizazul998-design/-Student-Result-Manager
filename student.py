
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display_info(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.name)


# Testing
student1 = Student("232431038", "Izazul Haque")

student1.display_info()
