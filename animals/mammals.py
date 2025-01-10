from animals import Animals


class Mammal(Animals):
    def __init__(self, name, escale=False):
        super().__init__(name)
        self.can_escale = escale
        self._scaling = False

    def get_attributes(self):
        return {
            'name': self.name,
            'weight': self.weight,
            'height': self.height,
            'can_fly': self.can_escale
        }
    
    def escale(self,target):
        if self.can_escale:
            self._scaling = True
            return print(f"The {self.name} is scaling a {target}")
        else:
            return print(f'The {self.name} cannot scaling a {target}')
        
    def moviment(self):
        return print(f"The {self.name} It's running")
    
    # O decorador @classmethod é usado para definir um método de classe. 
    # Um método de classe recebe a própria classe como primeiro argumento, 
    # geralmente chamado de 'cls'. Isso permite que o método acesse e modifique 
    # o estado da classe, ao invés de instâncias individuais da classe.
    @classmethod
    def make_humam(cls):
        human = cls('Human', True)
        human.set_attributes( 70, 1.70)
        return human