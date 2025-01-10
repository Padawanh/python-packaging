
from abc import ABC, abstractmethod

class Animals(ABC):
    def __init__(self, name):
        # print('Animals class created')
        self.name = name
        self.weight = None
        self.height = None
        self._wainting = True

        
    def __str__(self):
        return 'This is the Animals class'


    def set_attributes(self, weight, height):
        self.weight = weight
        self.height = height
        
    '''
    O decorador @abstractmethod é usado em Python para definir métodos abstratos 
    dentro de uma classe base abstrata. Um método abstrato é um método que é 
    declarado, mas não contém implementação. As subclasses que herdam da classe 
    base abstrata são obrigadas a implementar todos os métodos abstratos.
    '''
    @abstractmethod
    def moviment(self):
        pass
    
    @abstractmethod
    def get_attributes(self):
        pass