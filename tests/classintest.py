class Dog():
    def __init__(self, name):
        self.name = name

class Cat():
    def __init__(self, name):
        self.name = name

a_list = []
for x in range(3):
    a_list.append(Dog('Boris'))

b_list = []
for x in range(3):
    b_list.append(Cat('Igor'))

c_list = []
for x in range(3):
    c_list.append(Dog('Billy'))
    c_list.append(Cat('Bobby'))

print(b_list)

for x in b_list:
    if isinstance(x, Dog):
        print('I am a dog!')

for x in range(7):
    count = 0
    if x < 3:
        count = 2
    print(str(count))

for i in (a_list, b_list, c_list):
    hasdog = 0
    for x in i:
        if not isinstance(x, Dog):
            
            print('Not dog!')
        else:
            hasdog = 1
            print('Dog!')
            #break
    if hasdog == 1:
        print('This list has a dog!')
    else:
        print('This list does not have a dog!')
        
