
class Course:
    def __init__(self, course_code, title, credit):
        self.course_code = course_code
        self.title = title
        self.credit = credit

    def display_info(self):
        print("Course Code:", self.course_code)
        print("Course Title:", self.title)
        print("Credit:", self.credit)


class CourseManager:
    def __init__(self):
        self.courses = {}

    def add_course(self, course_code, title, credit):
        if course_code in self.courses:
            print("Error: Course already exists!")
            return

        if credit <= 0:
            print("Error: Credit must be positive!")
            return

        course = Course(course_code, title, credit)
        self.courses[course_code] = course

        print("Course added successfully!")

    def show_courses(self):
        if not self.courses:
            print("No courses found!")
            return

        for course in self.courses.values():
            course.display_info()
            print("-------------------")


# Testing
manager = CourseManager()

manager.add_course("CSE402", "Software Engineering", 3)
manager.add_course("CSE403", "Database Management", 3)
manager.add_course("CSE402", "Software Design", 3)

print("\nCourse List:")
manager.show_courses()
