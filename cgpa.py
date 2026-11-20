
class CGPACalculator:

    @staticmethod
    def calculate_cgpa(student_id, results, courses):

        total_points = 0
        total_credits = 0

        for key, result in results.items():

            sid, course_code = key

            if sid == student_id:

                if course_code not in courses:
                    continue

                credit = courses[course_code]["credit"]
                grade_point = result["grade_point"]

                total_points += grade_point * credit
                total_credits += credit

        if total_credits == 0:
            print("No results found!")
            return None

        cgpa = total_points / total_credits

        return round(cgpa, 2)


# Testing

courses = {
    "CSE402": {"credit": 3},
    "CSE403": {"credit": 3},
    "CSE404": {"credit": 1}
}

results = {
    ("101", "CSE402"): {
        "marks": 85,
        "grade": "A+",
        "grade_point": 4.00
    },

    ("101", "CSE403"): {
        "marks": 75,
        "grade": "A",
        "grade_point": 3.75
    },

    ("101", "CSE404"): {
        "marks": 60,
        "grade": "B",
        "grade_point": 3.00
    }
}

cgpa = CGPACalculator.calculate_cgpa(
    "101", results, courses
)

print("Student ID: 101")
print("CGPA:", cgpa)
