class Person:
    pi=3.1415
    def __init__(self, name):
        self.name=name

misko = Person("Misko")
katka = Person("Katka")

# class attribute je ten isty pre pristup z objeku a z triedy
print(misko.pi)
print(katka.pi)
print(Person.pi)

# Instace attr existuje len pre objekt 
print(misko.name)
print(katka.name)
# print(Person.name) # this is an error

# Ak je class attribute typu imutable tak po jeho zmene sa sa premeni na instancny attributa zmeni sa len pre dany objekt
misko.pi = 4 
print(misko.pi)
print(katka.pi)
print(Person.pi)

# Ak menime cez triedu zmeni sa vsade
# interne sa atribut hlada najprv v objekte a potom v triede ked sa nenajde v objekte 
Person.pi = 4 
print(misko.pi)
print(katka.pi)
print(Person.pi)


# Mutable attribut triedy 
class Person:
    pi=[]
    def __init__(self, name):
        self.name=name

misko = Person("Misko")
katka = Person("Katka")

# class attribute je ten isty pre pristup z objeku a z triedy
print(misko.pi)
print(katka.pi)
print(Person.pi)

misko.pi.append(4)
print(misko.pi)
print(katka.pi)
print(Person.pi)

# Pristup k class atributom vo funkcii 
class Employee:
    base_salary = 500
    def print_base_salary(self):
        # print(base_salary) # error
        print(self.base_salary)
        print(Employee.base_salary)
        # Changing through class
        Employee.base_salary = 600
        print(self.base_salary)
        print(Employee.base_salary)
        # changing through self
        self.base_salary = 700
        print(self.base_salary)
        print(Employee.base_salary)

    

emp = Employee()
emp.print_base_salary()