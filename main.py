
from student import Student
from course import CourseManager
from result import Result
from cgpa import CGPACalculator

students = {}
course_manager = CourseManager()
result_manager = Result()


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    if student_id in students:
        print("Student already exists!")
        return

    students[student_id] = Student(student_id, name)
    print("Student added successfully!")


def add_course():
    code = input("Enter Course Code: ")
    title = input("Enter Course Title: ")

    try:
        credit = float(input("Enter Course Credit: "))
        course_manager.add_course(code, title, credit)
    except ValueError:
        print("Invalid credit!")


def enter_marks():
    student_id = input("Enter Student ID: ")
    code = input("Enter Course Code: ")

    if student_id not in students:
        print("Student not found!")
        return

    if code not in course_manager.courses:
        print("Course not found!")
        return

    try:
        marks = float(input("Enter Marks: "))
        result_manager.enter_marks(student_id, code, marks)
    except ValueError:
        print("Invalid marks!")


def show_result():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found!")
        return

    students[student_id].display_info()

    found = False

    for key, result in result_manager.results.items():
        sid, code = key

        if sid == student_id:
            found = True
            course = course_manager.courses[code]

            print("\nCourse:", course.title)
            print("Course Code:", code)
            print("Marks:", result["marks"])
            print("Grade:", result["grade"])
            print("Grade Point:", result["grade_point"])

    if found:
        cgpa = CGPACalculator.calculate_cgpa(
            student_id,
            result_manager.results,
            course_manager.courses
        )
        print("\nCGPA:", cgpa)
    else:
        print("No results found!")


def main():
    while True:
        print("\n===== STUDENT RESULT MANAGER =====")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enter Marks")
        print("4. Show Result Sheet")
        print("5. Show All Students")
        print("6. Show All Courses")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_course()
        elif choice == "3":
            enter_marks()
        elif choice == "4":
            show_result()
        elif choice == "5":
            for student in students.values():
                student.display_info()
        elif choice == "6":
            course_manager.show_courses()
        elif choice == "7":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
