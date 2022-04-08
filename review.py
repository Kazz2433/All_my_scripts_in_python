peoples=['joao','maria','neto']
print(peoples)
print('Welcome to the party '+peoples[0] )
print('Welcome to the party '+peoples[1] )
print('Welcome to the party '+peoples[2] )
print('unfurtunately '+peoples[2].title()+ ' not come over today :(')
peoples.remove('neto')
peoples.append('junior')
print('Welcome to the party '+peoples[0] )
print('Welcome to the party '+peoples[1] )
print('Welcome to the party '+peoples[2] )
peoples.insert(0,'juan')
peoples.insert(2,'roberto')
peoples.append('rodolfo')
print('Welcome to the party '+peoples[0] )
print('Welcome to the party '+peoples[2] )
print('Welcome to the party '+peoples[-1] )
print('unfortunately, again, we could call only 2 persons to dinner, sorry')
print(peoples)
n0=peoples.pop(0)
n1=peoples.pop(1)
n2=peoples.pop(2)
n3=peoples.pop(-3)
print('Sorry, you was retired to dinner '+ n0 )
print('Sorry, you was retired to dinner '+ n1 )
print('Sorry, you was retired to dinner '+ n2 )
print('Sorry, you was retired to dinner '+ n3 )
print('\n ')
print(peoples)
del peoples[0]
del peoples[-1]
print('\n')
print(peoples)









