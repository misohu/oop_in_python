# OVERLOADING 
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def say_hello(self, name=None):
        print("Hello") if not name else print(f"Hello {self.name}")

person = Person("Michal" ,"Hucko")
person.say_hello()
person.say_hello(name=True)


# V jave sa nedaju pouzit optional parametre preto sa tam vyuziva nieco taketo 
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
    
#     def say_hello(self):
#         print("Hello") 
    
#     def say_hello(self, name=True):
#         print(f"Hello {self.name}") # TOTO sa vsak neda pouzit v pythone lebo nevieme deklarovat dve funkcie s rovnakymi nazvami 

# OVERRIDING
class Employee(Person):
    def say_hello(self):
        print("I am person and i will say something completely different than Person")

# Vsimnite si ze z rodica viem vytvorit kolko len vetiev chcem
class Student(Person):
    def __init__(self, name, surname, studentId):
        super().__init__(name,surname)
        self.studentId = studentId

student = Student("Michal", "Hucko", 106)
print(student.studentId)
student.say_hello()
