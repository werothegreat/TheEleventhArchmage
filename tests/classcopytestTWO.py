from classcopytest import Dog

class Dachsund(Dog):
    breed = 'dachsund'
    def __init__(self, name):
        Dog.__init__(self, name)

class Breeder(Dog):
    breed = 'breeder'
    def __init__(self, name):
        Dog.__init__(self, name)

    def breed(self, dog, alist):
        dogcopy = dog.copy()
        alist.append(dogcopy)

yep = Dachsund('Snoopy')
doglist = []
doglist.append(yep)
yop = yep.copy()
yes = Breeder('Billy')

print(doglist)

doglist.append(yep.copy())

print(doglist)

yes.breed(yep, doglist)

for x in doglist:
    print(str(x.virtual))
