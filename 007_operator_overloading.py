class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return self.name + " " + self.surname

    def __add__(self, other):
        return Marriage(self, other)
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __neg__(self):
        temp = Person(self.name, self.surname, self.age)
        temp.age = -1*temp.age
        return temp

class Marriage:
    def __init__(self, husband, wife):
        self.husband = husband
        self.wife = wife 
    
    def __str__(self):
        return self.husband.name + " + " + self.wife.name + "  " + self.husband.surname

michal = Person("Michal", "Hucko", 24)
katka  = Person("Katka", "Huckova", 60)

print(michal + katka)
print(michal == katka)
print((-michal).age)
print(michal.age) # POZOR objekt sa meni inplace

# __sub__(self, other) -> -
# __mul__(self, other) -> *
# __truediv__(self, other) -> /
# __floordiv__(self, other) -> //
# __mod__(self, other) -> %
# __pow__(self, other) -> **

# __lt__(self, other) -> <
# __gt__(self, other) -> >
# __le__(self, other) -> <=
# __ge__(self, other) -> >=
# __ne__(self, other) -> !=
