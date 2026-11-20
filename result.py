
from grade_calculator import GradeCalculator


class Result:
    def __init__(self):
        self.results = {}

    def enter_marks(self, student_id, course_code, marks):

        if not isinstance(marks, (int, float)):
            print("Error: Marks must be a number!")
            return

        if marks < 0 or marks > 100:
            print("Error: Marks must be between 0 and 100!")
            return

        key = (student_id, course_code)

        if key in self.results:
            print("Error: Marks already entered!")
            return

        grade, point = GradeCalculator.get_grade(marks)

        self.results[key] = {
            "marks": marks,
            "grade": grade,
            "grade_point": point
        }

        print("Marks entered successfully!")

    def show_result(self, student_id, course_code):

        key = (student_id, course_code)

        if key not in self.results:
            print("Result not found!")
            return

        result = self.results[key]

        print("Student ID:", student_id)
        print("Course Code:", course_code)
        print("Marks:", result["marks"])
        print("Grade:", result["grade"])
        print("Grade Point:", result["grade_point"])


# Testing
result_manager = Result()

result_manager.enter_marks("101", "CSE402", 85)
result_manager.show_result("101", "CSE402")


