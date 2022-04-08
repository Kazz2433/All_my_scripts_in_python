import json

filename = 'number_fav.json'
fav = str(input('Qual seria seu numero favorito? '))
with open(filename, 'w') as f_obj:
    json.dump(fav, f_obj)