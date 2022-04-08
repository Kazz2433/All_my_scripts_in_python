import json

filename = 'number_favs.json'
try:
    with open(filename) as f_obj:
        fav = json.load(f_obj)
except FileNotFoundError:
    pass
else:
    fav = str(input('Qual seria seu numero favorito? '))
    with open(filename, 'w') as f_obj:
        json.dump(fav, f_obj)


