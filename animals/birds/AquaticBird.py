from animals.birds import Bird


class Aquatic_Bird(Bird):
    """
    A class to represent an aquatic bird.
    Attributes:
    ----------
    name : str
        The name of the bird.
    can_fly : bool
        Indicates if the bird can fly.
    _swimming : bool
        Indicates if the bird is swimming.
    _environment : str
        The environment where the bird is typically found.
    Methods:
    -------
    get_attributes() -> dict:
        Returns a dictionary of the bird's attributes.
    fly() -> None:
        Sets the bird's flying status to True and prints a message.
    swim() -> None:
        Sets the bird's swimming status to True and prints a message.
    walk() -> None:
        Prints a message indicating the bird is walking.
    transit() -> None:
        Determines if the bird can fly or walk and prints the appropriate message.
    status() -> None:
        Prints the current status of the bird (flying, swimming, or walking).
    """

    def __init__(self, name: str, can_fly: bool) -> None:
        super().__init__(name, can_fly)
        self.can_fly = can_fly
        self._swimming = False
        self._environment = 'water'
        self._status = 'wainting'

    def get_attributes(self) -> dict:
        return {
            'name': self.name,
            'weight': self.weight,
            'height': self.height,
            'can_fly': self.can_fly
        }

    def fly(self) -> None:
        if self.can_fly:
            self._flaing = True
            self._wainting = False
            self._status = 'flying'
            return print(f"The {self.name} It's flying")
        else:
            self._wainting = False
            print(f"I cannot fly.")
            return self.walk()

    def swim(self) -> None:
        if self._environment == 'water':
            self._swimming = True
            self._status = 'swimming'
            return print(f"The {self.name} It's swimming")
        else:
            if self._environment == 'ground':
                self.walk()
                return print(f"The {self.name} It's in the wrong environment")

    def walk(self) -> None:
        self._walking = True
        self._wainting = False
        self._status = 'walking'
        self._environment = 'ground'
        return print(f"The {self.name} It's walking")

    def moviment(self) -> None:
        if self._environment == 'water':
            return self.swim()
        elif self._environment == 'ground':
            return self.walk()
        else:
            return self.fly()

    def status(self) -> None:
        return print(f"The {self.name} It's {self._status} in the {self._environment}")
