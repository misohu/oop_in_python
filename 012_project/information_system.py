from personal import Student, Teacher
from course import Course

class InformationSystem:
    def __init__(self, courses=[], students=[], teachers=[]):
        self.courses=courses
        self.students=students
        self.teachers=teachers
    
    def create_student(self):
        print("Student details:")
        while True:
            try:
                name=input("Name: ")
                surname=input("Surname: ")
                grade=input("Grade: ")
                print("Choose your course")
                for counter, course in enumerate(self.courses):
                    print(f"{counter}, {course}")
                course_id=int(input("Course id: "))
                if course_id <0 or course_id>=len(self.courses):
                    raise Exception("Please choose course from above")
            except Exception as e:
                print(e)
                print("Error during student creation please reenter details")
                continue
            break
        student=Student(name, surname, grade)
        self.courses[course_id].add_student(student)
        self.students.append(student)
    
    def create_teacher(self):
        print("Teacher details:")
        while True:
            try:
                name=input("Name: ")
                surname=input("Surname: ")
                degree=input("Degree: ")
            except Exception as e:
                print(e)
                print("Error during teacher creation please reenter details")
                continue
            break
        teacher=Teacher(name, surname, degree)
        self.teachers.append(teacher)

    def create_course(self):
        print("Course details:")
        while True:
            try:
                name=input("Name: ")
                counter = 0 
                print("Choose your teacher")
                for teacher in self.teachers:
                    print(f"{counter}, {teacher}")
                    counter +=1
                teacher_id=int(input("Teacher id: "))
                if teacher_id <0 or teacher_id>=len(self.teachers):
                    raise Exception("Please choose teachers from above")
            except Exception as e:
                print(e)
                print("Error during teacher creation please reenter details")
                continue
            break
        course = Course(name, self.teachers[teacher_id])
        self.courses.append(course)