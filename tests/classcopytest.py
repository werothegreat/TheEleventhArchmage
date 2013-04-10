from random import shuffle
import copy

class Dog(object):
    count = 0
    species = 'dog'
    def __init__(self, name):
        self.name = name
        Dog.count += 1 #using class title instead of self changes it for all
        self.id = self.count
        self.virtual = False
    def give_name(self):
        print('Hi, my name is {0}!'.format(self.name))
    def give_species(self):
        print('I am a {0}!'.format(self.species))
    def give_id(self):
        print('I am #{0}!'.format(self.id))
    def copy(self):
        copied_dog = copy.copy(self)
        copied_dog.virtual = True
        return copied_dog

'''class Kennel(object):
    def __init__(self, thingtype, count, name):
        self.animals = []
        self.species = thingtype.species
        for i in range(count):
            self.animals.append(thingtype(name))

a_kennel = Kennel(Dog, 5, 'Boris')
for x in range(len(a_kennel.animals)):
    a_kennel.animals[x].give_name()
    a_kennel.animals[x].give_species()
    a_kennel.animals[x].give_id()
    print('Actual number is {0}.'.format(str(x+1)))

b_kennel = Kennel(Dog, 5, 'Eglantine')

a_kennel.animals.extend(b_kennel.animals)
shuffle(a_kennel.animals)
print('Shuffling!')

for x in range(len(a_kennel.animals)):
    a_kennel.animals[x].give_name()
    a_kennel.animals[x].give_species()
    a_kennel.animals[x].give_id()
    print(str(len(a_kennel.animals)))'''

