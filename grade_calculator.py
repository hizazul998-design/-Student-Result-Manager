
class GradeCalculator:

    @staticmethod
    def get_grade(marks):

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100!")

        if marks >= 80:
            return "A+", 4.00
        elif marks >= 75:
            return "A", 3.75
        elif marks >= 70:
            return "A-", 3.50
        elif marks >= 65:
            return "B+", 3.25
        elif marks >= 60:
            return "B", 3.00
        elif marks >= 55:
            return "B-", 2.75
        elif marks >= 50:
            return "C+", 2.50
        elif marks >= 45:
            return "C", 2.25
        elif marks >= 40:
            return "D", 2.00
        else:
            return "F", 0.00


# Testing
print("85 Marks:", GradeCalculator.get_grade(85))
print("76 Marks:", GradeCalculator.get_grade(76))
print("68 Marks:", GradeCalculator.get_grade(68))
print("35 Marks:", GradeCalculator.get_grade(35))
