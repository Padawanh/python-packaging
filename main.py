from animals import mammals
from animals.birds import Bird
from animals.birds import Aquatic_Bird

Lion = mammals.Mammal('Lion', False)

Lion.transit()
print(Lion.get_attributes())
print("Add atributes")
Lion.set_attributes(200, 2)
print(Lion.get_attributes())
Lion.escale('tree')

human = mammals.Mammal.make_humam()
print(human.get_attributes())
human.transit()
human.escale('tree')

bird = Bird('Eagle', True)
bird.transit()
print(bird.get_attributes())

duck = Aquatic_Bird('Duck', True)
duck.transit()
print(duck.get_attributes())