from animals.birds.AquaticBird import Aquatic_Bird
from animals import mammals
from animals.birds import Bird


print(50*"-")
Lion = mammals.Mammal('Lion', False)
Lion.moviment()
print(Lion.print_atributes())
print("Add atributes")
Lion.set_attributes(200, 2)
print(Lion.print_atributes())
Lion.escale('tree')

print(50*"-")
human = mammals.Mammal.make_humam()
print(human.print_atributes())
human.moviment()
human.escale('tree')

print(50*"-")
bird = Bird('Eagle', True)
bird.moviment()
print(bird.print_atributes())

print(50*"-")
duck = Aquatic_Bird('Duck', True)
duck.moviment()
print(duck.print_atributes())
duck.walk()


duck.status()