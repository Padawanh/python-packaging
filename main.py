from animals import mammals
from animals.birds import Bird

Lion = mammals.Mammal('Lion', False)

Lion.moviment()
print(Lion.get_attributes())
print("Add atributes")
Lion.set_attributes(200, 2)
print(Lion.get_attributes())
Lion.escale('tree')

human = mammals.Mammal.make_humam()
print(human.get_attributes())
human.moviment()
human.escale('tree')

bird = Bird('Eagle', True)
bird.moviment()
print(bird.get_attributes())

from animals.birds.AquaticBird import Aquatic_Bird
duck = Aquatic_Bird('Duck', True)
duck.moviment()
print(duck.get_attributes())
duck.walk()