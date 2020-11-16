# Pouzitie tkzvanych class local premennych  
# Python vyuziva takzvany mangling alebo zahmlievanie 
class Line:
    __center = 10
    slope = 3
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def __print_center(self):
        print(f"Line hi {Line._Line__center}")
    
    def print_coordinates(self):
        print(f"x: {self.__x} y: {self.__y}")


line = Line(3, 4)

print(line.slope)
# print(line.__center)  # premenna je neviditelna z vonku  tiez 
print(line._Line__center) # avsak par trikmi sa k nej vieme dostat 
print(line._Line__x) # pristup k instancnym premennym

# Funkcie
line.print_coordinates()
# line.__print_center() # toto je chyba lebo metoda zacinajuca __ je neviditelna zvonku
line._Line__print_center() # toto je OK
Line._Line__print_center(line) # Ak chc
print(line.__dict__)

# Ako je to s dedenim?
class SpecialLine(Line):
    pass

sl = SpecialLine(2, 2)
print(sl._Line__center)
# print(sl._SpecialLine__center) # Error
