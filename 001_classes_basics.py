# Priklad definicie triedy. Zbytocnej triedy
class Person:
    name = "Michal"
    def print_name():
        print(f"Name is {Person.name}")

Person.print_name()

# Trieda je nejaky predpis niecoho v tomto pripade je to predpis osoby kazda osoba ma meno a priezvisko
class Person:
    def __init__(self, name, surname):
        self.name=name
        self.surname=surname
    
    def introduce_yourself(self):
        print(f"Hi I am {self.name} {self.surname}")

michal = Person("Michal", "Hucko")
michal.introduce_yourself()
katka = Person("Katka", "Huckova")
katka.introduce_yourself()

# Volanie metody v konstruktore 
class Person:
    def __init__(self, name, surname):
        self.name=name
        self.surname=surname
        self.introduce_yourself()
    
    def introduce_yourself(self):
        print(f"Hi I am {self.name} {self.surname}")

michal = Person("Michal", "Hucko")
katka = Person("Katka", "Huckova")

# Co je to ten self ? Je to skratka v pythone zoberme si nasledujucu triedu
class Classroom:
    def __init__(self, student_number):
        self.student_number = student_number
    
    def get_info(self):
        print(f"Student number is {self.student_number}")

new_class = Classroom(10)
new_class.get_info() # sa vnutorne prepise na 
Classroom.get_info(new_class)

# !!!! Self v pripade prveho parametru funkcie sa nemusi volat self ale moze byt pouzite akekolvek meno
# Vacsinou sa pouziva self
class Classroom2:
    def __init__(self, student_number):
        self.student_number = student_number
    
    def get_info(another_self):
        print(f"Student number is {another_self.student_number}")

new_class = Classroom2(20)
new_class.get_info() # sa vnutorne prepise na 
