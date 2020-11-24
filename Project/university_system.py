from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    @abstractmethod
    def introduce_yourself(self):
        pass


class Student(Person):
    def __init__(self, name, surname, grade):
        super().__init__(name, surname)
        self.grade = grade
    
    def introduce_yourself(self):
        print(f"Hi my name is {self.name} {self.surname} and I am in {self.grade}th")
    
    def __str__(self):
        return f"Student, name: {self.name}, surname: {self.surname}, grade: {self.grade}"


class Teacher(Person):
    def __init__(self, name, surname, degree):
        super().__init__(name, surname)
        self.degree = degree
    
    def introduce_yourself(self):
        print(f"Hi my name is {self.degree} {self.name} {self.surname}")
    
    def __str__(self):
        return f"Teacher, name: {self.name}, surname: {self.surname}, degree: {self.degree}"

class Course:
    def __init__(self, name, teacher, students=None): 
        self.name = name
        self.teacher = teacher
        self.__students = students if students else []

    def add_student(self, student):
        self.__students.append(student)
    
    def remove_student_by_surname(self, surname):
        self.__students = list(filter(lambda student: student.surname != surname, self.__students))
    
    def __str__(self):
        student_delimiter = "\n"
        return f"""{self.name}\nTaught by:\n{self.teacher}\n{student_delimiter.join([student.__str__() for student in self.__students])}"""
    

class InformationSystem:
    def __init__(self, courses=None, students=None, teachers=None):
        self.courses = courses if courses else []
        self.students = students if students else []
        self.teachers = teachers if teachers else []
    
    def create_student(self):
        print("Student details")
        while True:
            try:
                name = input("Name: ")
                surname = input("Surname: ")
                grade = input("Grade: ")
                for index, course in enumerate(self.courses):
                    print(f"{index}, {course.name}")
                course_id = int(input("Course number: "))
                if course_id < 0 or course_id >= len(self.courses):
                    raise Exception("Please choose from given courses")
            except Exception as e:
                print(e)
                print("Error during student input please reaenter the details")
                continue
            break
        student=Student(name, surname, grade)
        self.students.append(student)
        self.courses[course_id].add_student(student)
    
    def create_teacher(self):
        print("Teachers details")
        while True:
            try:
                name = input("Name: ")
                surname = input("Surname: ")
                degree = input("Degree: ")
            except Exception as e:
                print(e)
                print("Error during student input please reaenter the details")
                continue
            break
        self.teachers.append(Teacher(name, surname, degree))
    
    def create_course(self):
        print("Course details")
        while True:
            try:
                name = input("Name: ")
                for index, teacher in enumerate(self.teachers):
                    print(f"{index}, {teacher.__str__()}")
                teacher_id = int(input("Teacher number: "))
                if teacher_id < 0 or teacher_id >= len(self.teachers):
                    raise Exception("Please choose from given teachers")
            except Exception as e:
                print(e)
                print("Error during course input please reenter the details")
                continue
            break
        self.courses.append(Course(name, self.teachers[teacher_id]))

def print_menu():
    print("\n*******************************************")
    print("Vitajte v systeme")
    print("Stlačte prosím:")
    print("\t[0] Pre pridanie učiteľa")
    print("\t[1] Pre pridanie kurzu")
    print("\t[2] Pre pridanie žiaka")
    print("\t[3] Pre ukončenie práce so systémom")
    print("\t[4] Pre zoznam kurzov")
    print("\t[5] Pre zoznam ziakov")
    print("\t[6] Pre zoznam ucitelov")

teacher_michal = Teacher("Michal", "Hucko", "ing")
information_system = InformationSystem(
    [Course("Matchs", teacher_michal)],
    None,
    [
        teacher_michal,
        Teacher("Andrej", "Hucko", "ing")
    ]
)

while True:
    print_menu()
    try:
        menu_choice = int(input("Vaša voľba: "))
        if menu_choice < 0 or menu_choice > 6:
            raise Exception("Volba mimo menu")
    except Exception as e:
        print(e)
        print("Prosim zopakujte volbu")
        continue
    if menu_choice == 3:
        print("Dovidenia")
        break
    elif menu_choice == 0:
        information_system.create_teacher()
    elif menu_choice == 1:
        information_system.create_course()
    elif menu_choice == 2:
        information_system.create_student()
    elif menu_choice == 4:
        print("Kurzy v systeme")
        for course in information_system.courses:
            print(course)
    elif menu_choice == 5:
        print("Ziaci v systeme")
        for student in information_system.students:
            print(student)
    elif menu_choice == 6:
        print("Ucitelia v systeme")
        for teacher in information_system.teachers:
            print(teacher)
