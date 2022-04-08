def make_album(nome, album, qtd=''):
    perdon = {'Artista': nome, 'Album': album,}
    if perdon:
        perdon['qtd'] = qtd
    return perdon
d = 0
while d <= 3:
    d += 1
    a = input('Artista: ')
    b = input('Album: ')
    c = input('qtd: ')
    ele = make_album(a,b,c)
    print(ele)
 