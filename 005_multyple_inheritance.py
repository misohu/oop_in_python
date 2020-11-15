class Person:
    def __init__(self, name, surname):
        self.name = name 
        self.surname = surname
    
    def say_hi(self):
        print("Hi")

class Employee:
    def say_hello(self):
        print("Hello")

class Manager(Person, Employee):
    pass

manager = Manager("Michal", "Hucko")
manager.say_hi()
manager.say_hello()

# The diamond problem pre super class atributy 
class A:
    name = "A"
class B(A):
    name = "B"
    def __init__(self, b):
        self.b = b
class C(A):
    name = "C"
    def __init__(self, c):
        self.c = c
class D(C,B):
    name = "D"
    def get_super(self):
        print(super().name)

d = D("text")
d.get_super()
# print(d.b) 
print(d.c)


# Solution is the inheritance liearization applied as method resolution order
# # mro method 
# print(D.mro())
# print(list.mro())
# print(int.mro())
# print(bool.mro())
# print(float.mro())
# print(tuple.mro())
