roberto={
    'tipo':'cachorro',
    'dono':'quida',  
}
chat={
    'tipo':'gato',
    'dono':'quasdasdadadida',
}
oiseau={
    'tipo':'passaro',
    'dono':'sad',
}
pets=[roberto,chat,oiseau]
for k in pets:
    if k['tipo']=='cachorro':
        print('cachorro tem lingua pra fora')
    if k['tipo']=='gato':
        print('gato lingua pra dentro')
    if k['tipo']=='passaro':
        print('passaro a voar')
    