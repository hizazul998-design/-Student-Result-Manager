
import unittest

from grade_calculator import GradeCalculator
from result import Result
from course import CourseManager
from cgpa import CGPACalculator


class TestStudentResultManager(unittest.TestCase):

    def test_grade_calculation(self):
        self.assertEqual(
            GradeCalculator.get_grade(85), ("A+", 4.00)
        )

    def test_fail_grade(self):
        self.assertEqual(
            GradeCalculator.get_grade(35), ("F", 0.00)
        )

    def test_invalid_marks(self):
        with self.assertRaises(ValueError):
            GradeCalculator.get_grade(105)

    def test_enter_marks(self):
        manager = Result()
        manager.enter_marks("101", "CSE402", 85)

        self.assertIn(("101", "CSE402"), manager.results)

    def test_invalid_result_marks(self):
        manager = Result()
        manager.enter_marks("101", "CSE402", 110)

        self.assertNotIn(("101", "CSE402"), manager.results)

    def test_add_course(self):
        manager = CourseManager()
        manager.add_course("CSE402", "Software Engineering", 3)

        self.assertIn("CSE402", manager.courses)

    def test_cgpa_calculation(self):
        courses = {
            "CSE402": {"credit": 3},
            "CSE403": {"credit": 3}
        }

        results = {
            ("101", "CSE402"): {"grade_point": 4.00},
            ("101", "CSE403"): {"grade_point": 3.00}
        }

        cgpa = CGPACalculator.calculate_cgpa(
            "101", results, courses
        )

        self.assertEqual(cgpa, 3.50)


if __name__ == "__main__":
    unittest.main()
