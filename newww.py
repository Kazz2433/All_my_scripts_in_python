favorite_language = {
    "Renato": "C",
    "Baby": ['PHP','JS'],
    "Jorge": ['Java', 'COBOL']
}#certa

for k,v in favorite_language.items():#certa
    if len(v) <= 1:
        print("A favorita programing languages de " +k.title())
    else:
        print("As favoritas programing languages de "+k.title() )
    for i in v:
        print("\t"+ i)