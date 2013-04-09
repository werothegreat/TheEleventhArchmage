from classcopytest import Dog

class Dachsund(Dog):
    breed = 'dachsund'
    def __init__(self, name):
        Dog.__init__(self, name)

yep = Dachsund('Snoopy')
yop = yep.copy()

print(yop.name)
