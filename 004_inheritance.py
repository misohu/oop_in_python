class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def say_hi(self):
        print(f"Hi my name is {self.name} {self.surname}")
    
    def greet(self):
        print("Hi")

class Manager(Employee):
    def __init__(self, name, surname, department):
        Employee.__init__(self, name, surname)
        self.department = department
    
    def say_hi(self):
        super().say_hi()
        print(f"I am a Manager and my department is {self.department}")
    
    def say_departmnet(self):
        print(f"My department is {self.department}")

    
manager = Manager("Michal", "Hucko", "Informatika")
employee = Employee("Lukas", "Velky")
manager.say_hi()
manager.greet()
manager.say_departmnet()
# employee.say_departmnet() # this is an error

print("Instances")
print(isinstance(manager, Manager))
print(isinstance(manager, Employee))
print(isinstance(employee, Manager))
print(isinstance(employee, Employee))

print("Subclasses")
print(issubclass(Employee, Manager))
print(issubclass(Manager, Employee))


# Multilevel inheritance
class VicePrezident(Manager):
    def give_order(self):
        print("I give order")

# vice_prezident = VicePrezident() # error konstruktor sa zdedil implicitne
vice_prezident = VicePrezident("Michal", "Hucko", "Informatika")
vice_prezident.say_hi()
vice_prezident.say_departmnet()
vice_prezident.give_order()