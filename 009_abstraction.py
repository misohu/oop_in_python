from abc import ABC, abstractmethod

class Pc(ABC):
    @abstractmethod
    def __init__(self, keyboard, mouse):
        pass

    def boot(self):
        print("Booting")

    @abstractmethod
    def vrm_vrm(self):
        print("Vrm rm")
    
    @property
    @abstractmethod
    def cores_number(self):
        pass
    
    @cores_number.setter
    @abstractmethod
    def cores_number(self, value):
        pass

class Macbook(Pc):
    def __init__(self, keyboard, cores_number): # Loose abstraction parameters .... staci zadefinovat len metodu nie parametre
        self.keyboard = keyboard
        # self.mouse = mouse
        self.cores_number = cores_number

    def vrm_vrm(self):
        print("Vrm vrm")
    
    @property
    def cores_number(self):
        print("Using getter cores_number")
        return self._cores_number
    
    @cores_number.setter
    def cores_number(self, value):
        print("Using setter cores_number")
        if value < 0:
            raise ValueError("Valsue is bellow 0")
        self._cores_number = value

pc = Macbook(True, 10)
print(pc.cores_number)
print(pc.keyboard)

# pc.vrm_vrm()
# pc.boot()
# print(pc.keyboard)