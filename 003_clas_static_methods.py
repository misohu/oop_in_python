# Class metoda sa viaze na triedu a nie na objekt a tym padom na jej volanie nepotrebujeme objekt
# Jednym z parametrov class emtody je samotna trieda ... vdaka tomu vieme v class metode pracovat s class atributmi
# Class metoda je vlastne static metoda v jave !!!!
class Employee:
    base_salary = 400

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    @classmethod
    def get_base_salary(cls):
        print(f"Base salary is {cls.base_salary}")

Employee.get_base_salary()
emp = Employee("Michal", "Hucko")
emp.get_base_salary()


# Niekedy sa da pouzit class metona na takzvane faktory metody 
# To znamena ze clasmetoda vrati uz objekt danej triedy na zaklade inych argumentov ako su argumrnty konstruktoru
from datetime import date

class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    
    @classmethod
    def based_on_year(cls, name, year):
        return cls(name, date.today().year - year)

student = Student.based_on_year("Michal", 1996)
print(student.age)
    
# Samozrejme to sa da napisat aj bez toho takto 
class BetterStudent:
    def __init__(self, name, age=None, year=None):
        self.name = name
        self.age = date.today().year - year if year else age

student = BetterStudent("Michal", year=1996)
print(student.age)

# Static method nie je statick metoda v jave
# Staticka methoda v pythone nevie nic o triede a teda nevie pracovat s jej class metodami alebo parametrami 
class Husband:
    happy = True 
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def sum_numbers(num1, num2): # kedze nedostavam triedu ako parameter neviem k nej pristupit
        return num1 + num2

print(Husband.sum_numbers(1, 2))
misko = Husband("misko")
print(misko.sum_numbers(1, 2))
# staticka metoda pomaha zlepit funkciu k triede aj ked ju funkcia neovplyvnuje
