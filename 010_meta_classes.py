class Person: 
    pass

person = Person()
# Objekt je objekt 
print(type(person))
print(type(3))

# Trieda je objekt typu type
print(type(Person))
print(type(int))

# A type je typu type 
print(type(type))

# Ako sa rodia triedy? pomocou meta triedy type :O 
# type(<name>, <bases>, <dct>):
# meno 
# zoznam rodicov Tuple 
# zoznam menneho priestoru ... teda premennych a metod Dictionary 
A = type("A", (), {})
a = A()
print(a)

# class A:
#     pass

def multiline_method(self):
    print(f"X is {self.x}")

B = type("B", (A,), {"x": 10, "get_x": lambda self: self.x, "multiline_method": multiline_method})

b = B()
print(b)
print(b.get_x())
b.multiline_method()


# Vlastne Meta classy 
# factory class .... Nikto to nepouziva :D 
class Meta(type):
    def __init__(cls, name, bases, dict):
        print("New class is born")
        cls.Pi = 3.14

class Circle(metaclass=Meta):
    pass

# print(Circle.Pi)