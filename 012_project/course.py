class Course:
    def __init__(self, name, teacher=None, students=[]):
        self.name=name
        self.teacher=teacher
        self.students=students
    
    def add_student(self, student):
        self.students.append(student)
    
    def __str__(self):
        dalimiter="\n\t"
        return f"Course {self.name}\n\t{self.teacher}\n\t{dalimiter.join([student.__str__() for student in self.students])}"
