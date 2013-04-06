class Pencil(object):
    lead = 2
    def __init__(self):
        pass
    def give_lead(self):
        print(str(self.lead))

ticon = Pencil()
ticon.give_lead()

#success!  I can just 'pass' an __init__ method!
