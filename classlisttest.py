class Dog(object):
    species = 'dog'
    def __init__(self, name):
        self.name = name
    def give_name(self):
        print('Hi, my name is {0}!'.format(self.name))
    def give_species(self):
        print('I am a {0}!'.format(self.species))

class Cat(object):
    species = 'cat'
    def __init__(self, name):
        self.name = name
    def give_name(self):
        print('Hi, my name is {0}!'.format(self.name))
    def give_species(self):
        print('I am a {0}!'.format(self.species))

class Kennel(object):
    def __init__(self, thingtype, count, name):
        self.animals = []
        self.species = thingtype.species
        for i in range(count):
            self.animals.append(thingtype(name))

a_kennel = Kennel(Dog, 5, 'Boris')
for x in range(len(a_kennel.animals)):
    a_kennel.animals[x].give_name()
    a_kennel.animals[x].give_species()

a_kennel = Kennel(Cat, 5, 'Boris')
for x in range(len(a_kennel.animals)):
    a_kennel.animals[x].give_name()
    a_kennel.animals[x].give_species()
        
    
