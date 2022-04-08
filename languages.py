favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],   
}

for k, v in sorted(favorite_languages.items()):
    """ Definindo se os valores sao plurais os singulares"""
    if len(v) <=1:
        print('\n' + k.title() + ' favorite languague are:')
    else:
        print('\n' + k.title() + ' favorite languagues are:')

    """Printando os valores de cada pessoa"""
    for languages in v:
        print('\t '+ languages.title())