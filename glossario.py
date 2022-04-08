from collections import OrderedDict
from random import randint

class Die():

    def __init__(self,sides=randint(1,6)):
        self.sides=sides

    def roll_die(self):
        print(self.sides)

'''
glo = {'laço':'repetição','variavel':'conjunt de variaveis','python':'legal'}

a = OrderedDict()
a['laço'] = 'repetição'
a['variavel'] = 'conjunto de variaveis'
a['pytohn'] = 'legal'

for k,v in a.items():
    print(k.title() + " é " + v.title())
'''
a = Die()
a.roll_die()
