from animals import Animals


class Bird(Animals):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly
        self._flaing = False
        self._walking = False
        self._environment = 'ground'

    def get_attributes(self):
        return {
            'name': self.name,
            'weight': self.weight,
            'height': self.height,
            'can_fly': self.can_fly
        }

    def print_atributes(self):
        for keys, values in self.get_attributes().items():
            print(f'{keys} : {values}')

    def moviment(self):
        if self.can_fly:
            self._flaing = True
            return print(f"The {self.name} It's flying")
        else:
            self._wainting = False
            return print(f"I cannot fly. The {self.name} it's walking")
