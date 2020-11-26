from abc import ABC, abstractmethod

class Pc(ABC):
    @abstractmethod
    def __init__(self, keyboard, mouse):
        pass

    def boot(self):
        print("I am booting")

    @abstractmethod
    def vrm_vrm(self):
        pass

    @property
    @abstractmethod
    def keyboard(self):
        pass

    @keyboard.setter
    @abstractmethod
    def keyboard(self, value):
        pass

class Macbook(Pc):
    def __init__(self, cores_number, keyboard):
        self.cores_number = cores_number
        self.keyboard = keyboard

    def vrm_vrm(self):
        print("Vrm vrm mac")

    @property
    def cores_number(self):
        print("Getter called")
        return self._cores_number
    
    @cores_number.setter
    def cores_number(self, value):
        print("Setter called")
        if value <= 0:
            raise ValueError("cores_number must be positive only")
        self._cores_number = value 
    
    @property
    def keyboard(self):
        print("Getter called")
        return self._keyboard
    
    @keyboard.setter
    def keyboard(self, value):
        print("Setter called")
        self._keyboard = value 

pc = Macbook(2, True)

# pc.vrm_vrm()
# pc.boot()
# print(pc.keyboard)