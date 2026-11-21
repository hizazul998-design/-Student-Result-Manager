
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

                course = courses[course_code]

                credit = (
                    course.credit
                    if hasattr(course, "credit")
                    else course["credit"]
                )

                grade_point = result["grade_point"]

                total_points += grade_point * credit
                total_credits += credit

        if total_credits == 0:
            return None

        return round(total_points / total_credits, 2)
